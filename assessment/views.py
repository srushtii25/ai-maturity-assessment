from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib import messages
import json
import uuid
from .models import AssessmentResponse, User
from .questions import ASSESSMENT_QUESTIONS
from .pdf_generator import PDFGenerator

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        name = request.POST.get('name')
        company_name = request.POST.get('company_name')
        
        # Validate password confirmation
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return render(request, 'signup.html')
        
        user_model = User()
        result = user_model.create_user(email, password, name, company_name)
        
        if result['success']:
            messages.success(request, 'Account created successfully! Please login.')
            return redirect('login')
        else:
            messages.error(request, result['message'])
    
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user_model = User()
        user = user_model.authenticate(email, password)
        
        if user:
            request.session['user_id'] = user['user_id']
            request.session['user_name'] = user['name']
            request.session['user_company'] = user.get('company_name', '')
            messages.success(request, f'Welcome back, {user["name"]}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid email or password')
    
    return render(request, 'login.html')

def logout(request):
    request.session.flush()
    messages.success(request, 'Logged out successfully')
    return redirect('home')

def dashboard(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    
    assessment = AssessmentResponse()
    user_assessments = assessment.get_user_assessments(user_id)
    
    # Calculate stats
    total_assessments = len(user_assessments)
    completed_assessments = sum(1 for a in user_assessments if a.get('is_complete', False))
    incomplete_assessments = total_assessments - completed_assessments
    
    context = {
        'user_name': request.session.get('user_name'),
        'assessments': user_assessments,
        'total_assessments': total_assessments,
        'completed_assessments': completed_assessments,
        'incomplete_assessments': incomplete_assessments
    }
    
    return render(request, 'dashboard.html', context)

def start_assessment(request):
    user_id = request.session.get('user_id')
    if not user_id:
        messages.warning(request, 'Please login to save your assessment')
        return redirect('login')
    
    # Always start a new assessment when this view is called
    # The continue functionality should use continue_assessment view instead
    session_id = str(uuid.uuid4())
    request.session['assessment_id'] = session_id
    request.session['current_category'] = 0
    request.session['current_question'] = 0
    
    return redirect('question')

def question(request):
    session_id = request.session.get('assessment_id')
    if not session_id:
        return redirect('start_assessment')
    
    # Check if assessment is already complete
    assessment = AssessmentResponse()
    if assessment.is_assessment_complete(session_id):
        return redirect('results')
    
    current_category = request.session.get('current_category', 0)
    current_question = request.session.get('current_question', 0)
    
    categories = list(ASSESSMENT_QUESTIONS.keys())
    
    if current_category >= len(categories):
        return redirect('results')
    
    category = categories[current_category]
    category_questions = ASSESSMENT_QUESTIONS[category]
    question_keys = list(category_questions.keys())  # ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']
    
    if current_question >= len(question_keys):
        request.session['current_category'] = current_category + 1
        request.session['current_question'] = 0
        return redirect('question')
    
    question_key = question_keys[current_question]
    question_data = category_questions[question_key]
    
    # Check if this question was already answered
    assessment = AssessmentResponse()
    responses = assessment.get_responses(session_id)
    current_answer = None
    
    for response in responses:
        # Handle HTML encoding in stored category names
        stored_category = response['category'].replace('&amp;', '&')
        if stored_category == category and response['question_id'] == question_key:
            # Find the option key that matches this answer
            selected_key = None
            for key, option in question_data['options'].items():
                if option['text'] == response['answer']:
                    selected_key = key
                    break
            current_answer = {
                'text': response['answer'], 
                'score': response['score'],
                'key': selected_key
            }
            break
    
    context = {
        'session_id': session_id,
        'category': category,
        'category_index': current_category,
        'total_categories': len(categories),
        'question': question_data['question'],
        'question_id': question_key,
        'options': question_data['options'],
        'question_index': current_question,
        'total_questions': len(question_keys),
        'progress': ((current_category * 5 + current_question) / (len(categories) * 5)) * 100,
        'current_answer': current_answer
    }
    
    return render(request, 'questions.html', context)

@csrf_exempt
def save_answer(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            session_id = data.get('session_id')
            category = data.get('category')
            question_id = data.get('question_id')
            answer = data.get('answer')
            score = data.get('score')
            user_id = request.session.get('user_id')
            
            if not all([session_id, category, question_id, answer, score]):
                return JsonResponse({'status': 'error', 'message': 'Missing required fields'})
            
            assessment = AssessmentResponse()
            result = assessment.save_response(session_id, category, question_id, answer, score, user_id)
            
            return JsonResponse({'status': 'success', 'saved': True})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def next_question(request):
    current_question = request.session.get('current_question', 0)
    request.session['current_question'] = current_question + 1
    return redirect('question')

def previous_question(request):
    current_category = request.session.get('current_category', 0)
    current_question = request.session.get('current_question', 0)
    
    if current_question > 0:
        # Go to previous question in same category
        request.session['current_question'] = current_question - 1
    elif current_category > 0:
        # Go to last question of previous category
        request.session['current_category'] = current_category - 1
        request.session['current_question'] = 4  # Last question (0-indexed, 5 questions per category)
    
    return redirect('question')

def results(request):
    # Check if viewing a specific session from dashboard
    session_param = request.GET.get('session')
    if session_param:
        session_id = session_param
        # Verify user owns this session
        user_id = request.session.get('user_id')
        if not user_id:
            return redirect('login')
        
        assessment = AssessmentResponse()
        responses = assessment.get_responses(session_id)
        if not responses or responses[0].get('user_id') != user_id:
            messages.error(request, 'Assessment not found or access denied')
            return redirect('dashboard')
    else:
        # Current session results
        session_id = request.session.get('assessment_id')
        if not session_id:
            return redirect('start_assessment')
    
    assessment = AssessmentResponse()
    scores = assessment.calculate_scores(session_id)
    
    # Get prioritized top 3 strengths and opportunities
    from .questions import get_prioritized_categories
    strengths, opportunities = get_prioritized_categories(scores['category_scores'])
    
    context = {
        'scores': scores,
        'strengths': strengths,
        'opportunities': opportunities,
        'categories': list(scores['category_scores'].keys()),
        'user_company': request.session.get('user_company', 'Your Organization')
    }
    
    return render(request, 'results.html', context)

def radar_chart(request):
    # Check if viewing a specific session from dashboard
    session_param = request.GET.get('session')
    if session_param:
        session_id = session_param
        # Verify user owns this session
        user_id = request.session.get('user_id')
        if not user_id:
            return redirect('login')
        
        assessment = AssessmentResponse()
        responses = assessment.get_responses(session_id)
        if not responses or responses[0].get('user_id') != user_id:
            messages.error(request, 'Assessment not found or access denied')
            return redirect('dashboard')
    else:
        # Current session radar chart
        session_id = request.session.get('assessment_id')
        if not session_id:
            return redirect('start_assessment')
    
    assessment = AssessmentResponse()
    scores = assessment.calculate_scores(session_id)
    
    # Ensure consistent category ordering
    from .questions import ASSESSMENT_QUESTIONS
    ordered_categories = list(ASSESSMENT_QUESTIONS.keys())
    
    context = {
        'scores': scores,
        'categories': ordered_categories,
        'user_company': request.session.get('user_company', 'Your Organization')
    }
    
    return render(request, 'radar.html', context)

def continue_assessment(request, session_id):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    
    # Verify user owns this session
    assessment = AssessmentResponse()
    responses = assessment.get_responses(session_id)
    if not responses or responses[0].get('user_id') != user_id:
        messages.error(request, 'Assessment not found or access denied')
        return redirect('dashboard')
    
    # Check if assessment is already complete
    if assessment.is_assessment_complete(session_id):
        messages.info(request, 'This assessment is already complete. Viewing results instead.')
        return redirect(f'/results/?session={session_id}')
    
    # Set session variables to continue assessment
    request.session['assessment_id'] = session_id
    current_category, current_question = assessment.get_current_position(responses)
    request.session['current_category'] = current_category
    request.session['current_question'] = current_question
    
    return redirect('question')

def delete_assessment(request, session_id):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    
    assessment = AssessmentResponse()
    result = assessment.delete_assessment(session_id, user_id)
    
    if result.deleted_count > 0:
        messages.success(request, 'Assessment deleted successfully')
    else:
        messages.error(request, 'Assessment not found or access denied')
    
    return redirect('dashboard')

def next_steps(request):
    # Check if viewing a specific session from dashboard
    session_param = request.GET.get('session')
    if session_param:
        session_id = session_param
        # Verify user owns this session
        user_id = request.session.get('user_id')
        if not user_id:
            return redirect('login')
        
        assessment = AssessmentResponse()
        responses = assessment.get_responses(session_id)
        if not responses or responses[0].get('user_id') != user_id:
            messages.error(request, 'Assessment not found or access denied')
            return redirect('dashboard')
    else:
        # Current session next steps
        session_id = request.session.get('assessment_id')
        if not session_id:
            return redirect('start_assessment')
    
    assessment = AssessmentResponse()
    scores = assessment.calculate_scores(session_id)
    
    context = {
        'scores': scores,
        'maturity_level': scores.get('maturity_level', 'Emerging')
    }
    
    return render(request, 'next_steps.html', context)

def generate_pdf_report(request):
    # Check if viewing a specific session from dashboard
    session_param = request.GET.get('session')
    if session_param:
        session_id = session_param
        # Verify user owns this session
        user_id = request.session.get('user_id')
        if not user_id:
            return redirect('login')
        
        assessment = AssessmentResponse()
        responses = assessment.get_responses(session_id)
        if not responses or responses[0].get('user_id') != user_id:
            messages.error(request, 'Assessment not found or access denied')
            return redirect('dashboard')
    else:
        # Current session PDF
        session_id = request.session.get('assessment_id')
        if not session_id:
            return redirect('start_assessment')
    
    assessment = AssessmentResponse()
    scores = assessment.calculate_scores(session_id)
    
    # Create dimensions data structure for PDF with detailed content
    dimensions_data = {
        'AI Vision & Strategic Alignment': {
            'title': 'AI Vision & Strategic Alignment',
            'summary': 'Understand how clearly your company sees and steers its AI future.',
        },
        'Leadership & Governance': {
            'title': 'Leadership & Governance',
            'summary': 'Understand how well leadership supports, owns, and steers AI efforts.',
        },
        'Use Case Portfolio & Prioritization': {
            'title': 'Use Case Portfolio & Prioritization',
            'summary': 'Understand how AI is being used and scaled across your organization.',
        },
        'Data Infrastructure & Quality': {
            'title': 'Data Infrastructure & Quality',
            'summary': 'Assess how well the organization\'s data foundations and infrastructure support AI at scale',
        },
        'Talent & Culture': {
            'title': 'Talent & Culture',
            'summary': 'Understand if your teams are skilled, aligned, and culturally ready for AI.',
        },
        'Responsible AI & Risk': {
            'title': 'Responsible AI & Risk',
            'summary': 'Understand how responsibly and safely your organization builds and uses AI.',
        },
        'Measurement, Scaling & ROI': {
            'title': 'Measurement, Scaling & ROI',
            'summary': 'Understand how your organization tracks, scales, and learns from AI efforts.',
        },
        'AI Operating Model & Change Readiness': {
            'title': 'AI Operating Model & Change Readiness',
            'summary': 'Understand how your company is set up to support, scale, and sustain AI adoption.',
        },
        'Technology & AI Infrastructure': {
            'title': 'Technology & AI Infrastructure',
            'summary': 'Understand how well your tech stack supports building, running, and scaling AI.',
        }
    }
    
    # Generate PDF
    pdf_generator = PDFGenerator()
    user_company = request.session.get('user_company', 'Your Organization')
    pdf_buffer = pdf_generator.generate_pdf(scores, dimensions_data, session_id, user_company)
    
    # Create HTTP response
    response = HttpResponse(pdf_buffer.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="AI_Maturity_Assessment_Report_{session_id[:8]}.pdf"'
    
    return response
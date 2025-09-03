from pymongo import MongoClient
from django.conf import settings
from datetime import datetime
import uuid
import hashlib
import secrets

class MongoDBConnection:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.client = MongoClient(settings.MONGODB_URI)
            cls._instance.db = cls._instance.client[settings.MONGODB_NAME]
        return cls._instance

class User:
    def __init__(self):
        self.db = MongoDBConnection().db
        self.collection = self.db.users
    
    def create_user(self, email, password, name, company_name):
        # Check if user exists
        if self.collection.find_one({'email': email}):
            return {'success': False, 'message': 'Email already exists'}
        
        # Hash password
        salt = secrets.token_hex(16)
        password_hash = hashlib.sha256((password + salt).encode()).hexdigest()
        
        user = {
            'user_id': str(uuid.uuid4()),
            'email': email,
            'name': name,
            'company_name': company_name,
            'password_hash': password_hash,
            'salt': salt,
            'created_at': datetime.utcnow()
        }
        
        self.collection.insert_one(user)
        return {'success': True, 'user_id': user['user_id']}
    
    def authenticate(self, email, password):
        user = self.collection.find_one({'email': email})
        if not user:
            return None
        
        password_hash = hashlib.sha256((password + user['salt']).encode()).hexdigest()
        if password_hash == user['password_hash']:
            return {'user_id': user['user_id'], 'name': user['name'], 'email': user['email'], 'company_name': user.get('company_name', '')}
        return None
    
    def get_user(self, user_id):
        return self.collection.find_one({'user_id': user_id})

class AssessmentResponse:
    def __init__(self):
        self.db = MongoDBConnection().db
        self.collection = self.db.responses
    
    def save_response(self, session_id, category, question_id, answer, score, user_id=None):
        response = {
            'session_id': session_id,
            'category': category,
            'question_id': question_id,
            'answer': answer,
            'score': score,
            'user_id': user_id,
            'timestamp': datetime.utcnow()
        }
        return self.collection.update_one(
            {'session_id': session_id, 'category': category, 'question_id': question_id},
            {'$set': response},
            upsert=True
        )
    
    def get_responses(self, session_id):
        return list(self.collection.find({'session_id': session_id}))
    
    def get_user_assessments(self, user_id):
        # Get all unique sessions for a user
        pipeline = [
            {'$match': {'user_id': user_id}},
            {'$group': {
                '_id': '$session_id',
                'first_timestamp': {'$min': '$timestamp'},
                'last_timestamp': {'$max': '$timestamp'},
                'total_questions': {'$sum': 1}
            }},
            {'$sort': {'last_timestamp': -1}}
        ]
        results = list(self.collection.aggregate(pipeline))
        
        # Convert _id to session_id and determine completion status
        for result in results:
            result['session_id'] = result['_id']
            result['timestamp'] = result['last_timestamp']
            
            # Check if assessment has all 9 categories with 5 questions each (45 total)
            responses = self.get_responses(result['session_id'])
            unique_questions = set()
            for response in responses:
                # Handle HTML encoding in stored category names
                stored_category = response['category'].replace('&amp;', '&')
                unique_questions.add((stored_category, response['question_id']))
            
            result['unique_questions_answered'] = len(unique_questions)
            result['is_complete'] = len(unique_questions) >= 45  # 9 categories × 5 questions
            
        return results
    
    def calculate_scores(self, session_id):
        responses = self.get_responses(session_id)
        category_scores = {}
        category_raw_scores = {}
        
        # Group responses by category, handling HTML encoding
        for response in responses:
            # Handle HTML encoding in stored category names
            category = response['category'].replace('&amp;', '&')
            if category not in category_scores:
                category_scores[category] = []
                category_raw_scores[category] = []
            category_scores[category].append(response['score'])
            category_raw_scores[category].append(response['score'])
        
        # Calculate average scores per category (5 questions each, max 5.0 per category)
        category_averages = {}
        for category in category_scores:
            scores = category_scores[category]
            category_averages[category] = round(sum(scores) / len(scores), 1) if scores else 0
        
        # Sort categories by score (highest to lowest)
        sorted_categories = sorted(category_averages.items(), key=lambda x: x[1], reverse=True)
        
        # Calculate overall score (average of all category averages, max 5.0)
        overall_score_raw = sum(category_averages.values()) / len(category_averages) if category_averages else 0
        overall_score = round(overall_score_raw, 1)
        
        # Convert to 25-point scale for maturity stage determination
        # Average score × 5 = Stage score (as per your specification)
        stage_score = overall_score * 5
        
        # Get rule-based recommendations
        from .questions import evaluate_use_case_rules, get_maturity_stage_from_25_scale, AI_VISION_STAGE_PARAS
        recommendations = evaluate_use_case_rules(category_raw_scores)
        
        # Get maturity stage and description using 25-point scale
        maturity_stage = get_maturity_stage_from_25_scale(stage_score)
        stage_description = AI_VISION_STAGE_PARAS.get(maturity_stage, '')
        
        return {
            'category_scores': category_averages,
            'sorted_categories': sorted_categories,
            'overall_score': overall_score,
            'stage_score': round(stage_score, 1),
            'maturity_level': maturity_stage,
            'stage_description': stage_description,
            'recommendations': recommendations,
            'total_responses': len(responses),
            'unique_questions_answered': len(set((r['category'].replace('&amp;', '&'), r['question_id']) for r in responses))
        }
    

    
    def get_current_position(self, responses):
        """Calculate current category and question position based on responses"""
        from .questions import ASSESSMENT_QUESTIONS
        categories = list(ASSESSMENT_QUESTIONS.keys())
        
        # Group responses by category and question_id
        answered_questions = set()
        for response in responses:
            # Handle HTML encoding in stored category names
            stored_category = response['category'].replace('&amp;', '&')
            answered_questions.add((stored_category, response['question_id']))
        
        # If all questions are answered, redirect to results
        if len(answered_questions) >= 45:  # 9 categories × 5 questions
            return len(categories), 0  # This will trigger redirect to results
        
        # Find the first unanswered question
        for cat_idx, category in enumerate(categories):
            questions = ASSESSMENT_QUESTIONS[category]
            question_keys = list(questions.keys())  # ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']
            for q_idx, question_key in enumerate(question_keys):
                if (category, question_key) not in answered_questions:
                    return cat_idx, q_idx
        
        # All questions answered (fallback)
        return len(categories), 0
    
    def delete_assessment(self, session_id, user_id):
        """Delete all responses for a specific assessment session"""
        return self.collection.delete_many({
            'session_id': session_id,
            'user_id': user_id
        })
    
    def get_maturity_level(self, score):
        """Get maturity level based on average score (max 5.0) - DEPRECATED"""
        # This method is deprecated, use get_maturity_stage_from_25_scale instead
        stage_score = score * 5
        return self.get_maturity_stage_from_25_scale(stage_score)
    
    def is_assessment_complete(self, session_id):
        """Check if assessment is complete (all 45 questions answered)"""
        responses = self.get_responses(session_id)
        unique_questions = set()
        for response in responses:
            # Handle HTML encoding in stored category names
            stored_category = response['category'].replace('&amp;', '&')
            unique_questions.add((stored_category, response['question_id']))
        return len(unique_questions) >= 45  # 9 categories × 5 questions
    
    def get_maturity_stage_from_25_scale(self, stage_score):
        """Get maturity stage based on 25-point scale"""
        if 5 <= stage_score <= 9:
            return 'Nascent'
        elif 10 <= stage_score <= 14:
            return 'Emerging'
        elif 15 <= stage_score <= 19:
            return 'Scaling'
        elif 20 <= stage_score <= 24:
            return 'Transforming'
        elif stage_score >= 25:
            return 'Leading'
        else:
            return 'Nascent'
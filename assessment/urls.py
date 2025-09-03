from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('start/', views.start_assessment, name='start_assessment'),
    path('continue/<str:session_id>/', views.continue_assessment, name='continue_assessment'),
    path('delete/<str:session_id>/', views.delete_assessment, name='delete_assessment'),
    path('question/', views.question, name='question'),
    path('save-answer/', views.save_answer, name='save_answer'),
    path('next/', views.next_question, name='next_question'),
    path('previous/', views.previous_question, name='previous_question'),
    path('results/', views.results, name='results'),
    path('radar/', views.radar_chart, name='radar_chart'),
    path('next-steps/', views.next_steps, name='next_steps'),
    path('generate-pdf/', views.generate_pdf_report, name='generate_pdf_report'),
]
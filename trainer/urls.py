from django.urls import path
from . import views

app_name = 'trainer'

urlpatterns = [
    path('homepage_trainer/', views.homepage_trainer, name='homepage_trainer'),
    path('trainer/profile/', views.trainer_profile, name='trainer_profile'),
    path('trainer/assigned_employees/', views.assigned_employees, name='assigned_employees'),
    path('trainer/progress_report/<int:employee_id>/', views.progress_report, name='progress_report'),
]
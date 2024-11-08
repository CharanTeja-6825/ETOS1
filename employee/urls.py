from django.urls import path
from . import views

urlpatterns = [
    path('employee_homepage/', views.employee_dashboard, name='employee_homepage'),
]

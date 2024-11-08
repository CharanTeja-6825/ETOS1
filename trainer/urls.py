from django.urls import path
from . import views

urlpatterns = [
    path('trainer_homepage/', views.trainer_dashboard, name='trainer_homepage'),
]

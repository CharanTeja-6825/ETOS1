from django.urls import path
from . import views

app_name = 'trainer'

urlpatterns = [
    path('homepage_trainer/', views.homepage_trainer, name='homepage_trainer'),
]
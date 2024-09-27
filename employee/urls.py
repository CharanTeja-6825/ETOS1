from django.urls import path
from . import views

app_name = 'employee'

urlpatterns = [
  path('homepage_employee/', views.homepage_employee, name='homepage_employee'),
  path('profile/update/', views.update_profile, name='update_profile'),
  path('profile/password/', views.update_password, name='update_password'),
  path('profile/', views.profile_page, name='profile_page'),

]

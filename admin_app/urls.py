from django.urls import path
from . import views


app_name = 'admin_app'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('log_out/', views.log_out, name='log_out'),
    path('profile/', views.profile_page, name='profile_page'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('profile/password/', views.update_password, name='update_password'),

]

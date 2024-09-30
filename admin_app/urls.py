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
    path('course_manage/', views.Course_Manage, name='manage'),
    path('course_create/', views.create_course_view, name='course-create'),
    path('course_delete/', views.delete_course_view, name='course-delete'),
    path('course-update/<int:id>/', views.update_course_view, name='course-update'),

]


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
    path('courses/', views.course_list_view, name='course-list'),
    path('courses/new/', views.create_course, name='course-create'),
    path('courses/<int:pk>/edit/', views.course_update_view, name='course-update'),
    path('courses/<int:pk>/delete/', views.course_delete_view, name='course-delete'),
    path('courses/<int:course_id>/modules/new/', views.create_module, name='create-module'),
    path('courses/<int:course_id>/modules/<int:module_id>/edit/', views.edit_module, name='edit-module'),
]

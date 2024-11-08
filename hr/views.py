from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Course
from .forms import CourseForm

def HomePage(request):
    return render(request, 'project/project_homepage.html')  # Ensure 'home.html' is the name of your HTML file

def hr_dashboard(request):
    return render(request, 'hr/hr_homepage.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()

        # Redirect based on username format
        if username.isdigit() and len(username) == 4:
            return redirect('login')  # Replace with your URL
        elif username.isdigit() and len(username) == 10:
            return redirect('login')  # Replace with your URL
        else:
            return redirect('login')  # Replace with your URL

    return render(request, 'project/login_register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user using the default User model
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            # Redirect based on username format
            if username.isdigit() and len(username) == 4:
                return redirect('trainer_homepage')  # Replace with your URL
            elif username.isdigit() and len(username) == 10:
                return redirect('employee_homepage')  # Replace with your URL
            else:
                return redirect('hr_homepage')  # Replace with your URL
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'project/login_register.html')

def logout_view(request):
    logout(request)
    return redirect('homepage')

@login_required
def update_profile(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Get the current user
        user = request.user

        # Update user information
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        if email:
            user.email = email
        if password:
            user.set_password(password)
            update_session_auth_hash(request, user)  # Keep user logged in after password change

        # Save changes to the user
        user.save()
        messages.success(request, "Your profile has been updated successfully.")
        return redirect('home_redirect')  # Redirect to home page or another appropriate page

    else:
        context = {
            'user': request.user
        }
        return render(request, 'project/profile_update.html', context)

@login_required
def home_redirect(request):
    username = request.user.username
    if len(username) == 4:  # Trainer (4-digit username)
        return redirect('trainer_homepage')
    elif len(username) == 10:  # Employee (10-digit username)
        return redirect('employee_homepage')
    else:  # HR or others
        return redirect('hr_homepage')


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'hr/course_list.html', {'courses': courses})

# View to create a new course
def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'hr/course_form.html', {'form': form})

from django.shortcuts import get_object_or_404, redirect, render
from .models import Course  # Ensure you have imported your Course model

# View to delete a course
def course_delete(request, course_id):
    course = get_object_or_404(Course, id=course_id)  # Fetch the specific course

    if request.method == 'POST':
        course.delete()  # Delete the course
        return redirect('course_list')  # Redirect to the course list after deletion

    # Render a confirmation template if not a POST request
    return render(request, 'hr/course_list.html', {'course': course})

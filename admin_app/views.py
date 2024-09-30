from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth import logout
from django.db.models.functions import Length
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Course
from .forms import UpdatePasswordForm, CourseForm


def homepage(request):
    return render(request, 'admin_app/project_homepage.html')


def register(request):
    if request.method == 'POST':
        # Get form data
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Validate passwords
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')  # Replace 'register' with your registration page URL name

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
            return redirect('register')

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return redirect('register')

        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()

        messages.success(request, 'Registration successful. You can now log in.')
        return redirect('user_login')  # Replace 'user_login' with your login page URL name

    return render(request, 'admin_app/register.html')  # Replace 'admin_app/register.html' with your template path


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Check username length and redirect accordingly
            if len(username) == 10 and username.startswith('23000'):
                return redirect('employee:homepage_employee')  # Replace 'student_home' with the URL name for the student app homepage
            elif len(username) == 4:
                return redirect('trainer:homepage_trainer')
                # Replace 'faculty_home' with the URL name for the faculty app
            elif username.startswith('admin') and len(username) == 10:
                return redirect('admin_app:homepage')
            else:
                messages.error(request, 'Username length does not match any role-specific redirects.')
                return redirect('user_login')  # Redirect back to login if length does not match any criteria

        else:
            # If authentication fails, show an error message
            error_message = 'Invalid username or password. Please try again.'
            return render(request, 'admin_app/login.html', {'error_message': error_message})

    return render(request, 'admin_app/login.html')  # Render login page on GET request


def log_out(request):
    # Use Django's built-in logout function
    logout(request)

    # Redirect to a specific page after logging out (e.g., login page or homepage)
    return redirect(reverse('admin_app:homepage'))

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile_page')
    else:
        form = ProfileForm(instance=request.user)
        messages.error(request, 'An error occurred While performing the Action')

    return render(request, 'admin_app/profile.html', {'form': form})


def update_password(request):
    if request.method == 'POST':
        form = UpdatePasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Keep the user logged in
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile_page')
        else:
            print(form.errors)  # For debugging
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UpdatePasswordForm(user=request.user)

    return render(request, 'admin_app/profile.html', {'password_form': form})

@login_required
def profile_page(request):
    return render(request, 'admin_app/profile.html', {
        'user': request.user,
    })


def Course_Manage(request):
    return render(request, 'courses/CourseManagement.html')

def create_course_view(request):
    trainers = User.objects.filter(username__length=4)  # Filter trainers with username length 4
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'create_course.html', {'trainers': trainers, 'form': form})


def delete_course_view(request, pk):  # Use 'pk' instead of 'course_id' for standard naming
    course = get_object_or_404(Course, pk=pk)

    if request.method == 'POST':
        course.delete()
        messages.success(request, f'The course "{course.name}" was deleted successfully.')
        return redirect('course_list')  # Redirect to the course list view after deletion

    return render(request, 'delete_course.html', {'course': course})



def update_course_view(request, pk):
    course = get_object_or_404(Course, pk=pk)
    trainers = User.objects.filter(username__length=4)  # Get trainers with username length of 4

    if request.method == 'POST':
        # Update the course with POST data
        course.name = request.POST.get('name')
        course.description = request.POST.get('description')
        course.duration = request.POST.get('duration')
        course.trainer_id = request.POST.get('trainer')
        course.status = bool(request.POST.get('status'))

        # Save the updated course
        course.save()
        messages.success(request, f'The course "{course.name}" has been updated successfully.')
        return redirect('course_list')  # Redirect to the course list page after updating

    return render(request, 'update_course.html', {'course': course, 'trainers': trainers})

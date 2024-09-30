from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import ProfileForm, UpdatePasswordForm
from django.apps import apps

def homepage_employee(request):
    return render(request, 'employee/employee_homepage.html')

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('employee:profile_page')
    else:
        form = ProfileForm(instance=request.user)
        messages.error(request, 'An error occurred While performing the Action')

    return render(request, 'employee/employee_profile.html', {'form': form})


def update_password(request):
    if request.method == 'POST':
        form = UpdatePasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Keep the user logged in
            messages.success(request, 'Your password was successfully updated!')
            return redirect('employee:profile_page')
        else:
            print(form.errors)  # For debugging
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UpdatePasswordForm(user=request.user)

    return render(request, 'employee/employee_profile.html', {'password_form': form})

@login_required
def profile_page(request):
    return render(request, 'employee/employee_profile.html', {
        'user': request.user,
    })

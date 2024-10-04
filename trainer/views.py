from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.apps import apps
from django.shortcuts import render


def homepage_trainer(request):
    return render(request, 'trainer/trainer_homepage.html')


def assigned_courses(request):
    course = apps.get_model('admin_app', 'Course')
    trainer = request.user
    courses = course.objects.filter(trainer=trainer)
    return render(request, 'trainer/assigned_courses.html', {'courses': courses})


@login_required
def course_detail(request, course_id):
    course = apps.get_model('admin_app', 'Course')
    # Fetch the course based on the course_id and ensure the logged-in user is the assigned trainer
    course = get_object_or_404(course, id=course_id, trainer=request.user)

    # Render the course detail template with the course context
    return render(request, 'trainer/course_info.html', {'course': course})


def trainer_assigned_employees(request):
    # Dynamically load the Course and Employee models from another app
    Course = apps.get_model('admin_app', 'Course')
    Employee = apps.get_model('employee', 'EmployeeCourse')

    # Filter courses for the logged-in trainer
    trainer = request.user  # Assuming the logged-in user is the trainer
    courses = Course.objects.filter(trainer=trainer).select_related('employee')

    # Create a list of assigned employees
    employees = [course.employee for course in courses]

    context = {
        'employees': employees
    }
    return render(request, 'trainer/assigned_employees.html', context)

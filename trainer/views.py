from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.apps import apps


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

from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Trainer

def homepage_trainer(request):
    return render(request, 'trainer/trainer_homepage.html')


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required



# @login_required
# def trainer_profile(request):
#     # Get the trainer's profile (assuming each trainer has a user account)
#     trainer = get_object_or_404(Trainer, user=request.user)
#
#     if request.method == 'POST':
#         form = TrainerProfileForm(request.POST, instance=trainer)
#         if form.is_valid():
#             form.save()
#             return redirect('trainer_dashboard')  # Redirect after saving
#     else:
#         form = TrainerProfileForm(instance=trainer)  # Load current profile data
#
#     return render(request, 'trainer/profile.html', {'form': form})
#
#
#
#
# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from .models import TrainingSchedule
#
# @login_required
# def assigned_employees(request):
#     # Assuming the logged-in user is a trainer
#     schedules = TrainingSchedule.objects.filter(trainer=request.user)
#
#     return render(request, 'trainer/assigned_employees.html', {'schedules': schedules})
#
#
#
#
#
# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required
# from .models import Employee, ProgressReport
# from .forms import ProgressReportForm
#
# @login_required
# def progress_report(request, employee_id):
#     employee = get_object_or_404(Employee, id=employee_id)
#     reports = ProgressReport.objects.filter(employee=employee)
#
#     if request.method == 'POST':
#         report_id = request.POST.get('report_id')
#         report = get_object_or_404(ProgressReport, id=report_id)
#         form = ProgressReportForm(request.POST, instance=report)
#         if form.is_valid():
#             form.save()
#             return redirect('progress_report', employee_id=employee_id)
#     else:
#         form = ProgressReportForm()
#
#     return render(request, 'trainer/progress_report.html', {
#         'reports': reports,
#         'form': form
#    })
@login_required
def my_courses(request):
    try:
        trainer = Trainer.objects.get(user=request.user)
        courses = trainer.assigned_courses.all()  # Get the assigned courses
    except Trainer.DoesNotExist:
        # Handle the case where no Trainer object exists for the user
        courses = None  # Or any other fallback action, such as returning an empty course list

    return render(request, 'trainer/assigned_courses.html', {'courses': courses})



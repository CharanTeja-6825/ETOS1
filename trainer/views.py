from django.shortcuts import render

# Trainer Dashboard View
def trainer_dashboard(request):
    return render(request, 'trainer/trainer_homepage.html')

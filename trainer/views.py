from django.shortcuts import render


def homepage_trainer(request):
    return render(request, 'trainer/trainer_homepage.html')

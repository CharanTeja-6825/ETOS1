from django.shortcuts import render

# Employee Dashboard View
def employee_dashboard(request):
    return render(request, 'employee/employee_homepage.html')


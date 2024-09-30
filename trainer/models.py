from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Trainer(models.Model):
    # Assuming each trainer is linked to a user account
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField(blank=True)
    expertise = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name



from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class TrainingSchedule(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    trainer = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming each trainer is a User
    training_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f'{self.employee.name} - {self.training_date}'



from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class ProgressReport(models.Model):
    STATUS_CHOICES = [
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    remarks = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.employee.name} - {self.status}'


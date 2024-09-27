from django.db import models
from django.contrib.auth.models import User

class Courses(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User, related_name='enrolled_courses')

class Certificate(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, related_name='certificates', on_delete=models.CASCADE)

class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    expertise = models.CharField(max_length=100)

    def __str__(self):
        return self.user.get_full_name()

class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    duration = models.PositiveIntegerField(help_text="Duration in hours", null=True)
    trainer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='assigned_courses')
    status = models.BooleanField(default=True, help_text="Toggle to activate/deactivate the course")

    def __str__(self):
        return self.name


class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

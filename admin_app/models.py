from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.PositiveIntegerField()  # Duration in hours
    trainer = models.ForeignKey(User, limit_choices_to={'username__length': 4}, on_delete=models.SET_NULL, null=True)  # Trainer with username length 4
    status = models.BooleanField(default=True)  # Active/Inactive status

    def __str__(self):
        return self.name
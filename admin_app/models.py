from django.db import models
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.PositiveIntegerField()  # Duration in hours
    trainer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # Trainer linked to User
    status = models.BooleanField(default=True)  # Active/Inactive status

    def __str__(self):
        return self.name

    def clean(self):
        if self.trainer and len(self.trainer.username) != 4:
            raise ValidationError({'trainer': 'Trainer username must be exactly 4 characters long.'})

    def save(self, *args, **kwargs):
        self.clean()  # Call clean method before saving
        super().save(*args, **kwargs)

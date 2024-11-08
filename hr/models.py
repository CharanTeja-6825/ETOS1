from django.db import models

class Course(models.Model):
    serial_number = models.CharField(max_length=50, unique=True, help_text="A unique identifier for the course",
                                     null=True)
    course_name = models.CharField(max_length=200, help_text="Name of the course", null=True)
    duration = models.CharField(max_length=100, help_text="Duration of the course", null=True)
    description = models.TextField(blank=True, help_text="Optional detailed description of the course", null=True)
    created_at = models.DateTimeField(auto_now_add=True, help_text="The date and time when the course was created",
                                      null=True)

    def __str__(self):
        return self.course_name

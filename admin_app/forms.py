from django.contrib.auth.forms import PasswordChangeForm
from django import forms
from django.contrib.auth.models import User
from django import forms
from .models import Course

class UpdatePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput())
    new_password1 = forms.CharField(widget=forms.PasswordInput())
    new_password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'duration', 'trainer', 'status']

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        # Filter trainers with username length of 4
        self.fields['trainer'].queryset = User.objects.filter(username__length=4)
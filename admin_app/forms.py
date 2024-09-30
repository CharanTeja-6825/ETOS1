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
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter trainers whose username length is exactly 4 characters
        self.fields['trainer'].queryset = User.objects.filter(username__regex=r'^\w{4}$')
        # Debugging output
        print(self.fields['trainer'].queryset)  # This should print the filtered queryset

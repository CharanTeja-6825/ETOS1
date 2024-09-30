from django import forms
from .models import Trainer

class TrainerProfileForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['name', 'email', 'bio', 'expertise']  # Add relevant fields
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write a brief bio...'}),
            'expertise': forms.TextInput(attrs={'placeholder': 'Expertise area'}),
        }


from django import forms
from .models import TrainingSchedule

class TrainingScheduleForm(forms.ModelForm):
    class Meta:
        model = TrainingSchedule
        fields = ['employee', 'training_date', 'description']  # Add other fields if necessary



from django import forms
from .models import ProgressReport

class ProgressReportForm(forms.ModelForm):
    class Meta:
        model = ProgressReport
        fields = ['status', 'remarks']

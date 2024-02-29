from django import forms

from .models import Job, JobApplication

class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'summary', 'full_description']
        
        
class ApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['content', 'experience']
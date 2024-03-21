from django import forms

from .models import Job, JobApplication

class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'summary', 'full_description', 'company_name', 'company_location', 'company_country', 'company_size']
        
        
        
class ApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['content', 'experience']
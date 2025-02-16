from django import forms
from .models import Job, Application

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'description', 'location']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'email', 'resume', 'cover_letter']
from django import forms

from .models import Commission, Job, JobApplication


class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = "__all__"
        exclude = ["author"]

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = "__all__"
        exclude = ["commission"]


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = []

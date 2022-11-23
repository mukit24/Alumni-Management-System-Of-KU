from django import forms
from .models import Alumni_Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Alumni_Profile
        fields = [
            'full_name',
            'image',
            'certificate',
            'discipline',
            'student_id',
            'batch',
            'job_type',
            'job_position',
            'company_name',
            'higher_study',
            'present_address',
            'present_country',
            'parmanent_address',
            'mobile',
            'facebook',
            'linkdin',
            'about_me',
        ]

        labels = {
            "job_type": "Job Type(Optional):",
            "job_position": "Job Position(Optional):",
            "company_name": "Company Name(Optional):",
            "higher_study": "Higher Study(Degree & University)(Optional):",
            "facebook":"Facebook Link(Optional):",
            "linkdin":"Linkdin Link(Optional):",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
            'class': 'form-control mb-1'})
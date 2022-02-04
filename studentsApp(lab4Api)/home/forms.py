from django import forms
from home.models import student, Intake

class StudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ('fullname', 'email', 'password',)
        
        
class IntakeForm(forms.Form):
    intake_name=forms.CharField(max_length=100)
    start_date=forms.DateField()
    end_date=forms.DateField()


# your_app/forms.py
from django import forms
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'username', 'birth_of_date', 'phone_num', 'email', 'school', 'password']
        widgets = {
            'birth_of_date': forms.DateInput(attrs={'type': 'date'}),
            'password': forms.PasswordInput(),
        }

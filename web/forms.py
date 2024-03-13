# your_app/forms.py
from django import forms
from inab.models import User, Book, School, Borrow


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "genre",
            "pages",
            # "library",
        ]  # Add other fields as needed


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School

        fields = [
            "name",
        ]


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "password", "first_name", "last_name", "role"]
        widgets = {
            "password": forms.PasswordInput(),
        }


class BookRequestForm(forms.ModelForm):
    class Meta:
        model = Borrow

        fields = [
            "book",
            "borrowStatus",
            "date",
            "borrowReport",
            "student",
        ]

from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Book, Member, BookOrder, BookRent, BookPDF


class BookForm(ModelForm):

    class Meta:
        model = Book
        fields = ['name', 'description', 'author', 'genre', 'ageGroup',
                  'bookCopies', 'date_published', 'date_of_keeping']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Book Name'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Description'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Author'}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
            'ageGroup': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Age Group'}),
            'bookCopies': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Book Copies'}),

            'date_published': forms.DateTimeInput(format=('%m/%d/%Y'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'date_of_keeping': forms.DateTimeInput(format=('%m/%d/%Y'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
        }


class BookPdfForm(ModelForm):
    class Meta:
        model = BookPDF
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Book Name'}),
            'pdf': forms.FileInput(),
        }


class OrderForm(ModelForm):
    class Meta:
        model = BookOrder
        fields = '__all__'
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Book Name'}),
        #     'pdf': forms.FileInput(),
        # }


class RentForm(ModelForm):
    class Meta:
        model = BookRent
        fields = '__all__'


class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'email', 'phone',
                  'date_of_membership', 'age', 'profile_pic']
        # exclude = ['user']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'age': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Age'}),
            'date_of_membership': forms.DateTimeInput(format=('%m/%d/%Y'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'profile_pic': forms.FileInput(),
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

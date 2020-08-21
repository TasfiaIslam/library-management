from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Book, Member, BookOrder, BookRent, BookPDF

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class BookPdfForm(ModelForm):
    class Meta:
        model = BookPDF
        fields = '__all__'

class OrderForm(ModelForm):
    class Meta:
        model = BookOrder
        fields = '__all__'

class RentForm(ModelForm):
    class Meta:
        model = BookRent
        fields = '__all__'

class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        exclude = ['user']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
from django import forms
from .models import Customer,Employee
from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class EmployeeSignup(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['name','phone','age','gender','address','city',]

class CustomerSignup(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['name','age','city']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username' ,'email' , 'password1','password2']

class user_update(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class profile_pic_emp(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['image']

class profile_pic_cus(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['image']

class edit_detail_emp(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['name','phone','age','gender','address','city']

class edit_detail_cus(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['name','age','city']

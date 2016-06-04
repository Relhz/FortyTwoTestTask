# -*- coding: utf-8 -*-
from django import forms
from models import Info


class LoginForm(forms.Form):

    Username = forms.CharField(max_length=30)
    Password = forms.CharField(max_length=30, widget=forms.PasswordInput)


class EditForm(forms.ModelForm):

    Name = forms.CharField(max_length=20)
    Contacts = forms.CharField(max_length=50)
    Last_name = forms.CharField(label='Last name', max_length=20)
    Email = forms.EmailField(max_length=30)
    Date_of_birth = forms.DateField(label='Date of birth')
    Skype = forms.CharField(max_length=50)
    Photo = forms.ImageField()
    Jabber = forms.CharField(max_length=50)
    Other_contacts = forms.CharField(label='Other contacts', max_length=100, 
    	widget=forms.Textarea)
    Bio = forms.CharField(max_length=500, widget=forms.Textarea)

    class Meta:

        model = Info
        fields = ['Name', 'Contacts', 'Last_name', 'Email', 'Date_of_birth',
        'Skype', 'Photo', 'Jabber', 'Other_contacts', 'Bio']

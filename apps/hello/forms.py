# -*- coding: utf-8 -*-
from django import forms
from models import Info


class LoginForm(forms.Form):

    Username = forms.CharField(max_length=30)
    Password = forms.CharField(max_length=30, widget=forms.PasswordInput)


class EditForm(forms.ModelForm):

    Name = forms.CharField(max_length=30)
    Contacts = forms.CharField(max_length=50)
    Last_name = forms.CharField(label='Last name', max_length=30)
    Email = forms.EmailField(max_length=30)
    Date_of_birst = forms.DateField(label='Date of birst')
    Skype = forms.CharField(max_length=30)
    Photo = forms.ImageField()
    Jabber = forms.CharField(max_length=30)
    Other_contacts = forms.CharField(label='Other contacts', max_length=50, 
    	widget=forms.Textarea)
    Bio = forms.CharField(max_length=300, widget=forms.Textarea)

    class Meta:

        model = Info
        fields = ['Name', 'Contacts', 'Last_name', 'Email', 'Date_of_birst',
        'Skype', 'Photo', 'Jabber', 'Other_contacts', 'Bio']
# -*- coding: utf-8 -*-
from django import forms
from models import Info
from django.core.exceptions import ValidationError
import re


class LoginForm(forms.Form):

    Username = forms.CharField(max_length=30)
    Password = forms.CharField(max_length=30, widget=forms.PasswordInput)


class EditForm(forms.ModelForm):
    
    other_contacts = forms.CharField(max_length=100, 
        widget=forms.Textarea, required=False)
    bio = forms.CharField(max_length=500, widget=forms.Textarea,
                          required=False)

    class Meta:

        model = Info
        fields = ['name', 'contacts', 'last_name', 'email', 'date_of_birth',
        'skype', 'photo', 'jabber', 'other_contacts', 'bio']

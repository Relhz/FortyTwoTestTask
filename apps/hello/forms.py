# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from models import Info
from django.core.exceptions import ValidationError
import re


# only leters should be in the name
def validate_name(self):

    if re.match(r'^([a-zA-Zа-яА-Я]+)$', self.strip()):
        return
    raise ValidationError("Please, write only letters")


# only leters or single hyphen between words should be in the surname
def validate_last_name(self):
    if re.match(r'^([a-zA-Zа-яА-Я]+)([-]?)([a-zA-Zа-яА-Я]+)$', self.strip()):
        return
    raise ValidationError("Please, write only letters or single hyphen "
                              "between words if you have double surname")


class LoginForm(forms.Form):

    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)


class EditForm(forms.ModelForm):

    name = forms.CharField(validators=[validate_name], required=False)
    last_name = forms.CharField(validators=[validate_last_name])
    other_contacts = forms.CharField(max_length=100,
                                     widget=forms.Textarea, required=False)
    bio = forms.CharField(max_length=500, widget=forms.Textarea,
                          required=False)

    class Meta:

        model = Info
        fields = ['name', 'contacts', 'last_name', 'email', 'date_of_birth',
                  'skype', 'photo', 'jabber', 'other_contacts', 'bio']

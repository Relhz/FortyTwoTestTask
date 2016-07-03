# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from models import Info, Requests
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


# only number from 1 to 999 should be
def validate_priority(self):

    if re.match(r'^([1-9]|[0-9][0-9]|[0-9][0-9][0-9])$', str(self)):
        return
    raise ValidationError("Error: here should be number from 1 to 999")


class EditForm(forms.ModelForm):

    name = forms.CharField(validators=[validate_name], required=False)
    last_name = forms.CharField(validators=[validate_last_name])
    other_contacts = forms.CharField(max_length=100,
                                     widget=forms.Textarea, required=False)
    bio = forms.CharField(max_length=1000, widget=forms.Textarea,
                          required=False)

    class Meta:

        model = Info
        fields = ['name', 'contacts', 'last_name', 'email', 'date_of_birth',
                  'skype', 'photo', 'jabber', 'other_contacts', 'bio']


class PriorityForm(forms.ModelForm):

    priority = forms.IntegerField(validators=[validate_priority])

    class Meta:

        model = Requests
        fields = ['priority']

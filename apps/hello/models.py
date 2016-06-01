# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Info(models.Model):

    name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, default='Surname')
    date_of_birth = models.DateField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    contacts = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    skype = models.CharField(max_length=50, null=True, blank=True)
    jabber = models.CharField(max_length=50, null=True, blank=True)
    other_contacts = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.last_name

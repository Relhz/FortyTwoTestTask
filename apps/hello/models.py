# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Info(models.Model):

    name = models.CharField(max_length=10, null=True, blank=True)
    last_name = models.CharField(max_length=10, default='Surname')
    date_of_birst = models.DateField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    contacts = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    skype = models.CharField(max_length=50, null=True, blank=True)
    jabber = models.CharField(max_length=50, null=True, blank=True)
    other_contacts = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return str(self.last_name)


class Requests(models.Model):

    path = models.CharField(max_length=300, default='path')
    method = models.CharField(max_length=10, default='Post')
    date_and_time = models.DateTimeField(default=timezone.now())
    status_code = models.CharField(max_length=10, default='200')

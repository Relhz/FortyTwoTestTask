# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from PIL import Image, ImageOps
from django.core import validators


class Info(models.Model):

    name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, default='Surname')
    date_of_birth = models.DateField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    contacts = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(
        max_length=50,
        null=True,
        blank=True,
        validators=[validators.validate_email]
    )
    skype = models.CharField(max_length=50, null=True, blank=True)
    jabber = models.EmailField(
        max_length=50,
        null=True,
        blank=True,
        validators=[validators.validate_email]
    )
    other_contacts = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='photos',
        default="media/photos/no-avatar.jpg")

    # model object represents as last name str
    def __unicode__(self):
        return self.last_name

    def save(self, *args, **kwargs):
        super(Info, self).save(*args, **kwargs)
        if self.photo:
            photo = Image.open(self.photo)
            imagefit = ImageOps.fit(photo, (200, 200),
                                    Image.ANTIALIAS)
            imagefit.save(self.photo.path, 'JPEG', quality=75)


class Requests(models.Model):

    path = models.CharField(max_length=300, default='path')
    method = models.CharField(max_length=10, default='Post')
    requests_date_time = models.DateTimeField(auto_now=True, null=True)

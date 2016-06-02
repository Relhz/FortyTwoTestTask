# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import Info
from django.core.exceptions import MultipleObjectsReturned


def main(request):

    try:
        info, created = Info.objects.get_or_create(last_name='Kudrya')
    except MultipleObjectsReturned:
        info = Info.objects.filter(last_name='Kudrya').first()

    return render(request, 'hello/main.html', {'info': info})

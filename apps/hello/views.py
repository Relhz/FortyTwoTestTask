# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import Info
from django.core.exceptions import MultipleObjectsReturned


def main(request):

    info = Info.objects.all().first()
    
    return render(request, 'hello/main.html', {'info': info})

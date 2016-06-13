# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import Info


# main page displays persons information
def main(request):

    info = Info.objects.first()

    return render(request, 'hello/main.html', {'info': info})

from django.shortcuts import render
from models import Info


def main(request):

    info = Info.objects.all().first
    return render(request, 'base.html', {'info': info})

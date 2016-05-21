from django.shortcuts import render
from models import Info


def main(request):

    info = Info()
    return render(request, 'base.html', {'info': info})

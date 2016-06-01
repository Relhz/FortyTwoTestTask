from django.shortcuts import render
from models import Info


def main(request):

    info = Info.objects.all().first
    return render(request, 'hello/main.html', {'info': info})

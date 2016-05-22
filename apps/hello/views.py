from django.shortcuts import render
from models import Info


# main page displays persons information
def main(request):

    info = Info.objects.all().first
    return render(request, 'base.html', {'info': info})


# requests page displays last 10 requests
def ind(request):
    
    requests = (
        ('path', 'date and time'),
        ('path', 'date and time'),
        ('path', 'date and time'),
        ('path', 'date and time'),
        ('path', 'date and time'),
        ('path', 'date and time'),
        ('path', 'date and time'),
        ('path', 'date and time'),
        ('path', 'date and time'),
        ('path', 'date and time')
    )
    return render(request, 'hello/requests.html', {'requests': requests})
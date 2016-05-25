from django.shortcuts import render, HttpResponse, redirect
from models import Info
from models import Requests
from forms import LoginForm
from django.contrib import auth
import json


# count amount of the requests
class RequestsCounter():
    amount = 0


# main page displays persons information
def main(request):

    info = Info.objects.all().first
    RequestsCounter.amount += 1

    return render(request, 'base.html', {'info': info})


# requests page displays last 10 requests
def requests(request):

    objects = Requests.objects.all()
    requests = []
    for i in range(29, 19, -1):
        requests.append(objects[i])
    RequestsCounter.amount += 1

    return render(request, 'hello/requests.html', {'requests': requests})


def login(request):

    err = request.session.get('err')
    request.session['err'] = ''
    form = LoginForm()
    RequestsCounter.amount += 1
    return render(request, 'hello/login.html', {'form': form, 'err': err})


def log_in(request):

    if request.POST:
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['Username']
            password = form.cleaned_data['Password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('main')
            else:
                request.session['err'] = 'Incorrect username or password'
        else:
            request.session['err'] = 'Incorrect username or password'
            return redirect('login')
        return redirect('login')

    return redirect('login')


def logout(request):

    auth.logout(request)
    request.session['err'] = ''
    return redirect('main')


def edit(request):

    return HttpResponse


# return data from database to ajax function
def forajax(request):

    if request.method == 'GET':

        obj = Requests.objects.all().last()
        response_data = {}
        response_data['path'] = obj.path
        response_data['method'] = obj.method
        response_data['date_and_time'] = str(obj.date_and_time)
        response_data['status_code'] = obj.status_code
        response_data['count'] = Requests.objects.all().count()

    return HttpResponse(json.dumps(response_data),
                           content_type="application/json")


# return 10 objects from database to ajax function
def forajax2(request):

    if request.method == 'GET':

        objs = Requests.objects.all()[19:]
        ll = []

        for i in objs:
            response_data = {}
            response_data['path'] = i.path
            response_data['method'] = i.method
            response_data['date_and_time'] = str(i.date_and_time)
            response_data['status_code'] = i.status_code
            ll.append(response_data)

        ll.reverse()
    return HttpResponse(json.dumps(ll), content_type="application/json")


# return amount of the requests to ajax function
def forajax_count(request):

    if request.method == 'GET':
        if RequestsCounter.amount > 10:
            RequestsCounter.amount = 10
        c = {}
        c['amount'] = RequestsCounter.amount
    return HttpResponse(json.dumps(c), content_type="application/json")


# reset amount of the requests
def forajax_count_reset(request):

    if request.method == 'GET':
        RequestsCounter.amount = 0
    return HttpResponse()

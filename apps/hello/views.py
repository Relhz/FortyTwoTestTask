# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseBadRequest
from models import Info
from models import Requests
from forms import LoginForm
from forms import EditForm
from django.contrib import auth
import json
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from fortytwo_test_task.settings.common import log  # NOQA
import logging
logger = logging.getLogger('hello')


# main page displays persons information
def main(request):

    info = Info.objects.first()
    logger.debug('Variables: ' + str(info))

    return render(request, 'hello/main.html', {'info': info})


# requests page displays last 10 requests
def requests(request):

    if request.is_ajax():
        if request.method != 'GET':
            return HttpResponseBadRequest()
        else:
            # return last 10 objects from database
            objs = Requests.objects.all().order_by('-pk')[:10].values()
            return HttpResponse(json.dumps(list(objs), default=date_handler),
                                content_type="application/json")
    else:
        objects = Requests.objects.all().order_by('-pk')[:10]
        logger.debug('Variables: ' + str(objects))

    return render(request, 'hello/requests.html', {'objects': objects})


def date_handler(obj):

    return obj.isoformat() if hasattr(obj, 'isoformat') else obj


# login page
def login(request):

    err = request.session.get('err')
    if err == None: err = ''
    request.session['err'] = ''
    form = LoginForm()

    return render(request, 'hello/login.html', {'form': form, 'err': err})


def log_in(request):

    # if user loged in on the edit page, 
    # then redirect to the edit page, else - the to main page
    if request.session.get('redir') == 'edit':
        redir = '/edit/'
    else:
        redir = '/'

    if request.POST:
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['Username']
            password = form.cleaned_data['Password']
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect(redir)
            else:
                request.session['err'] = 'Incorrect username or password'
        else:
            request.session['err'] = 'Incorrect username or password'
            return redirect('/login/')
        return redirect('/login/')

    return redirect(redir)


def logout(request):

    auth.logout(request)
    request.session['err'] = ''
 
    return redirect('main')


# edit page
def edit(request):

    info = Info.objects.first()

    initial = {
        'Name': info.name,
        'Last_name': info.last_name,
        'Date_of_birth': info.date_of_birth,
        'photo': info.photo,
        'Contacts': info.contacts,
        'Email': info.email,
        'Skype': info.skype,
        'Jabber': info.jabber,
        'Bio': info.bio,
        'Other_contacts': info.other_contacts,

    }

    form = EditForm(initial=initial)
    loginform = LoginForm()
    request.session['redir'] = 'edit'
    
    return render(request, 'hello/edit.html',
                  {'form': form, 'loginform': loginform, 'info': info})


# edit data
@login_required
def forajax_edit(request):

    o = ''
    
    if request.method == 'POST':

        if request.is_ajax():
            form = EditForm(data=request.POST, files=request.FILES)
            if form.is_valid():
                
                info = Info.objects.first()

                info.name = request.POST.get('Name')
                info.last_name = request.POST.get('Last_name')
                info.date_of_birth = request.POST.get('Date_of_birth')
                info.contacts = request.POST.get('Contacts')
                info.email = request.POST.get('Email')
                info.skype = request.POST.get('Skype')
                info.jabber = request.POST.get('Jabber')
                info.bio = request.POST.get('Bio')
                info.other_contacts = request.POST.get('Other_contacts')
                info.photo = request.FILES.get('Photo')

                info.save()
            else:
                return HttpResponse(json.dumps(form.errors), content_type="application/json")

    return HttpResponse(json.dumps('o'), content_type="application/json")

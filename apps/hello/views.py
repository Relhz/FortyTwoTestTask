# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseBadRequest
from models import Info
from models import Requests
from forms import LoginForm
from forms import EditForm
from django.contrib import auth
import json
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

    if request.POST:
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('edit')
            else:
                request.session['err'] = 'Incorrect username or password'
        else:
            request.session['err'] = 'Incorrect username or password'

        return redirect('login')

    err = request.session.get('err')
    if err is None:
        err = ''
    request.session['err'] = ''
    form = LoginForm()

    return render(request, 'hello/login.html', {'form': form, 'err': err})


def logout(request):

    auth.logout(request)
    request.session['err'] = ''

    return redirect('main')


# edit page
@login_required
def edit(request):

    info = Info.objects.first()

    if request.method == 'POST':

        form = EditForm(data=request.POST, files=request.FILES, instance=info)
        if form.is_valid():
            form.save()
        return HttpResponse(json.dumps(form.errors),
                            content_type="application/json")
    if info:
        initial = {
            'name': info.name,
            'last_name': info.last_name,
            'date_of_birth': info.date_of_birth,
            'photo': info.photo,
            'contacts': info.contacts,
            'email': info.email,
            'skype': info.skype,
            'jabber': info.jabber,
            'bio': info.bio,
            'other_contacts': info.other_contacts,
        }
        form = EditForm(initial=initial)
    else:
        form = EditForm()

    return render(request, 'hello/edit.html', {'form': form, 'info': info})

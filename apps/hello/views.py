from django.shortcuts import render, HttpResponse, redirect
from models import Info
from models import Requests
from django.http import HttpResponseBadRequest
from forms import LoginForm
from forms import EditForm
from django.contrib import auth
import json
from django.utils import timezone


# main page displays persons information
def main(request):

    info = Info.objects.first()

    return render(request, 'hello/main.html', {'info': info})


# requests page displays last 10 requests
def requests(request):

    objects = Requests.objects.all().order_by('-pk')[:10]

    return render(request, 'hello/requests.html', {'objects': objects})


def date_handler(obj):

    return obj.isoformat() if hasattr(obj, 'isoformat') else obj


# return last 10 objects from database
def forajax(request):

    if request.method != 'GET':
        return HttpResponseBadRequest()
    else:
        objs = Requests.objects.all().order_by('-pk')[:10].values()

    return HttpResponse(json.dumps(list(objs), default=date_handler),
                        content_type="application/json")


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

    info = Info.objects.all().first()
    date = info.date_of_birth
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
    
    return render(request, 'hello/edit.html', {'form': form, 'loginform': loginform})


# edit data
def forajax_edit(request):

    o = ''
    if request.method == 'POST':
        if request.is_ajax():
            
            form = EditForm(data=request.POST, files=request.FILES)
            info = Info.objects.all().first()

            info.name = request.POST.get('name')
            info.last_name = request.POST.get('last_name')
            info.date_of_birth = request.POST.get('date_of_birth')
            info.contacts = request.POST.get('contacts')
            info.email = request.POST.get('email')
            info.skype = request.POST.get('skype')
            info.jabber = request.POST.get('jabber')
            info.bio = request.POST.get('bio')
            info.other_contacts = request.POST.get('other_contacts')
            info.photo = request.FILES.get('photo')

            info.save()

    return HttpResponse(json.dumps('o'), content_type="application/json")

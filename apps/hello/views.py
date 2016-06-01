from django.shortcuts import render, HttpResponse, redirect
from models import Info
from models import Requests
from forms import LoginForm
from forms import EditForm
from django.contrib import auth
import json
from django.utils import timezone

# main page displays persons information
def main(request):

    info = Info.objects.all().first()
    request.session['redir'] = ''

    return render(request, 'base.html', {'info': info})


# requests page displays last 10 requests
def requests(request):

    objects = Requests.objects.all()
    requests = []
    for i in range(29, 19, -1):
        requests.append(objects[i])

    return render(request, 'hello/requests.html', {'requests': requests})


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
    initial = {
        'Name': info.name,
        'Last_name': info.last_name,
        'Date_of_birst': info.date_of_birst,
        'Contacts': info.contacts,
        'Email': info.email,
        'Skype': info.skype,
        'Jabber': info.jabber,
        'Bio': info.bio,
        'Other_contacts': info.other_contacts,
        'Photo': info.photo
    }
    form = EditForm(initial=initial)
    loginform = LoginForm()
    request.session['redir'] = 'edit'
    
    return render(request, 'hello/edit.html', {'form': form, 'loginform': loginform})


# return last 10 objects from database
def forajax2(request):

    if request.method == 'GET':

        objs = Requests.objects.all()[19:]
        ll = []

        for i in objs:
            response_data = {}
            response_data['path'] = i.path
            response_data['method'] = i.method
            response_data['date_and_time'] = str(timezone.localtime(
                i.date_and_time
                ))
            response_data['status_code'] = i.status_code
            response_data['amount'] = i.pk
            ll.append(response_data)

        ll.reverse()
    return HttpResponse(json.dumps(ll), content_type="application/json")


# return amount of the requests
def forajax_count(request):

    if request.method == 'GET':

        c = {}
        c['amount'] = Requests.objects.all().last().pk

    return HttpResponse(json.dumps(c), content_type="application/json")


# edit data
def forajax_edit(request):

    if request.method == 'POST':

        info = Info.objects.all().first()

        info.name = request.name,
        info.last_name = request.last_name,
        info.date_of_birst = request.date_of_birst,
        info.contacts = request.contacts,
        info.email = request.email,
        info.skype = request.skype,
        info.jabber = request.jabber,
        info.bio = request.bio,
        info.other_contacts = request.other_contacts,
        info.photo = request.photo

        info.save()

        c = {'success': 'success'}

    return HttpResponse(json.dumps(c), content_type="application/json")

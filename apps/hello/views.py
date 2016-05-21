from django.shortcuts import render

def main(request):

    info = {'Name': 'Yevhen', 
    'Last name': 'Kudrya', 
    'Date of birst': '21-01-1990',
    'Bio': 'Yevhen Kudrya, Python-developer, Kharkiv, Ukraine. Was burn in Kharkiv on 21 January 1990. In 1993 relocated in Chuguiv, Kharkivska region. In septemper 1997 began to study at scool. In 2007 finished Chuguiv Gymnasium 5 and entered to National Technical University "Kharkiv Polytechnical Institute", machine building department. In June 2011 graduated with a Bachelor and in February 2013 with a Specialist. In February 2013 got a job as design-engineer at Kharkiv Tractor Plant. In March 2014 fired width personal reducing. In 2014 worked in freelance as copywriter. In 2015 began to learn coding',
    'Contacts': 'mob: 0502455842', 
    'Email': 'yevhenkudrya@gmail.com', 
    'Skype': 'seekandstrike',
    'Jabber': 'relhz@42cc.co', 
    'Other contacts': '--'}
    return render(request, 'base.html', {'info': info})
from django.conf.urls import patterns
from django.conf.urls import url
from . import views


urlpatterns = patterns(
    '',
    url(r'^$', views.main, name='main'),
    url(r'^requests/', views.requests, name='requests'),
    url(r'^edit/', views.edit, name='edit'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^log_in/', views.log_in, name='log_in'),
    url(r'^forajax_edit/', views.forajax_edit, name='forajax_edit'),

)

from django.conf.urls import url

from django.contrib import admin

from django.conf import settings

from . import views

urlpatterns =[
    url(r'^signup/$', views.signup, name='signup')
]
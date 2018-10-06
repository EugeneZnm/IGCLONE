from django.conf.urls import url

from django.contrib import admin

from django.conf import settings

from . import views

urlpatterns =[
    url(r'^profile_edit/',views.profile_edit,name='edit_profile'),
    url(r'^signup/$', views.signup, name='signup'),

    url(r'^profile/', views.profile, name='profile'),
]
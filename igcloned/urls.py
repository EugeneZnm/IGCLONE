from django.conf.urls import url

from django.contrib import admin

from django.conf import settings

from . import views

urlpatterns =[
    url(r'^signup/$', views.signup, name='signup'),

    url(r'^profile/', views.profile, name='profile'),

url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]
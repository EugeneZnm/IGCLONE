from django.conf.urls import url

from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns =[
    url(r'^profile_edit/',views.profile_edit,name='edit_profile'),
    url(r'^signup/$', views.signup, name='signup'),

    url(r'^profile/', views.profile, name='profile'),

    url(r'^home/', views.home, name='home'),

    url(r'^follow/(?P<operation>,+)/(?P<pk>\d+)/$', views.follower, name='follow'),

    url(r'^comment/(?P<image_id>\d+)', views.add_comment, name='comment'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
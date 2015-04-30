from django.conf.urls import patterns, url
from django.views.generic import ListView

from main.views import *
from main.models import *
urlpatterns = patterns('main.views',
        #Room homepage
        url(r'^$', RoomIndex.as_view()),
        #room urls
        url(r'^rooms/create$', RoomCreate.as_view()),
        url(r'^rooms/(?P<pk>\d+)$', RoomDetail.as_view()),
        url(r'^rooms/(?P<pk>\d+)/modify$', 'room_modify'),
        url(r'^rooms/(?P<pk>\d+)/delete$', 'room_delete'),
)

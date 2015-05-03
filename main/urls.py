from django.conf.urls import patterns, url
from django.views.generic import ListView

from main.views import *
from main.models import *
urlpatterns = patterns('main.views',
        #Room homepage
        url(r'^$',
                            RoomIndex.as_view(),name="room_home"),
        url(r'^rooms/create$', 
                            RoomCreate.as_view(),name="room_create"),
        url(r'^rooms/(?P<pk>\d+)$',
                            RoomDetail.as_view(),name="room_detail"),
        url(r'^rooms/(?P<pk>\d+)/update$',
                            RoomUpdate.as_view(),name="room_update"),
        url(r'^rooms/(?P<pk>\d+)/delete$',
                            RoomDelete.as_view(),name="room_delete"),
)

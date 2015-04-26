from django.conf.urls import patterns, url
from django.views.generic import ListView

from main.models import *
urlpatterns = patterns('main.views',
        #homepage
        url(r'^$', ListView.as_view(
                            model=Room,
                            queryset=Room.objects.all(),
                            context_object_name="rooms",
                            template_name='main/room_index.html')),
        
        #room urls
        #url(r'^rooms/create$', RoomCreateView.as_view()),
        url(r'^rooms/(?P<id>[0-9]+)$', 'room_detail', name='room_detail'),
        url(r'^rooms/(?P<id>[0-9]+)/modify$', 'room_modify', name='room_modify'),
        url(r'^rooms/(?P<id>[0-9]+)/delete$', 'room_delete', name='room_delete'),
)

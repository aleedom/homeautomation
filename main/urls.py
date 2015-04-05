from django.conf.urls import patterns, url

urlpatterns = patterns('main.views',
                #homepage
                url(r'^$', 'index', name='index'),
                
                #room urls
                url(r'^rooms$', 'room_list', name='room_list'),
                url(r'^rooms/create$', 'room_create', name='room_create'),
                url(r'^rooms/(?P<id>[0-9]+)$', 'room_detail', name='room_detail'),
                url(r'^rooms/(?P<id>[0-9]+)/modify$', 'room_modify', name='room_modify'),
                url(r'^rooms/(?P<id>[0-9]+)/delete$', 'room_delete', name='room_delete'),
)

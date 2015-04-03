from django.conf.urls import patterns, url

urlpatterns = patterns('main.views',
                #homepage
                url(r'^$', 'index', name='index'),
		#ex: /sensorsi
		url(r'^sensors$', 'list_sensors', name='list_sensors'),
		#ex /main/sensors/28-23434
		url(r'^sensors/(?P<serial>[\w{}.-]{1,15})$', 'detail_sensors',name='detail_sensors'),
)

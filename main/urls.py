from django.conf.urls import patterns, url

urlpatterns = patterns('main.views',
		#ex: /main/sensors
		url(r'^sensors$', 'list_sensors', name='list_sensors'),
		#ex /main/sensors/28-23434
		url(r'^sensors/(?P<serial>[\w{}.-]{1,15})$', 'detail_sensors',name='detail_sensors'),
)

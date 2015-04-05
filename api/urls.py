from django.conf.urls import patterns, url

urlpatterns = patterns(
	'api.views',
	url(r'^sensors$', 'Sensor_list', name='Sensor_list'),
	url(r'^sensors/(?P<serial>[\w{}.-]{1,15})$', 'Sensor_detail', name='Sensor_detail'),
	url(r'^data$', 'Data_post', name='Data_post'),
)

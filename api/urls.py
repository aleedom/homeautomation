from django.conf.urls import patterns, url

urlpatterns = patterns(
	'api.views',
	url(r'^tempsensor$', 'Tsensor_list', name='Tsensor_list'),
	url(r'^tempsensor/(?P<pk>[\w{}.-]{1,15})$', 'Tsensor_detail', name='Tsensor_detail'),
	url(r'^temperature/(?P<serial>[\w{}.-]{1,15})$', 'Temperature_list', name='Temperature_list'),
)

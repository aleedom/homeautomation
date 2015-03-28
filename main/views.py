from django.shortcuts import render

from main.models import Tsensor, Temperature


def list_sensors(request):
	sensor_list = Tsensor.objects.all()
	context = {'sensor_list': sensor_list}
	return render(request, 'main/sensor_list.html', context)


def detail_sensors(request, serial):
	temp_list = Temperature.objects.filter(serial=serial)
	context = {'temp_list':temp_list}
	return render(request, 'main/sensor_detail.html', context)

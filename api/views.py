import json

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from main.models import Tsensor, Temperature, Room
from api.serializers import TsensorSerializer, TemperatureSerializer


@api_view(['GET', 'POST'])
def sensor_list(request):
	"""
	list all ,or create a new temperature sensor
	"""
	if request.method == 'GET':
		sensors = Sensor.objects.all()
		serializer = SensorSerializer(sensors, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = SensorSerializer(data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(
					serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def sensor_detail(request, pk):
	"""
	Get, update, or delete a specific sensor
	"""
	sensor = {}
	try:
		sensor = Sensor.objects.get(pk=pk)
	except sensor.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method =='GET':
		serializer = TsensorSerializer(sensor)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = SensorSerializer(sensor, data=request.DATA)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(
					serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	elif request.method == 'DELETE':
		sensor.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def Data_list(request, serial):
	"""
	Get all data from one sensor or Post new Temperature data
	
	try:
		sensor = Tsensor.objects.get(pk=pk)
	except sensor.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
"""
	if request.method == 'GET':
		temps = Data.objects.filter(serial=serial)
		serializer = TemperatureSerializer(temps, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = TemperatureSerializer(data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(
					serializer.errors, status=status.HTTP_400_BAD_REQUEST)

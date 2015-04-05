import json

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from main.models import * 
from api.serializers import SensorSerializer, DataSerializer


@api_view(['GET', 'POST'])
def Sensor_list(request):
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
def Sensor_detail(request, serial):
	"""
	Get, update, or delete a specific sensor
	"""
	sensor = {}
	try:
		sensor = Sensor.objects.get(serial=serial)
	except sensor.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method =='GET':
		serializer = SensorSerializer(sensor)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = SensorSerializer(sensor, data=request.DATA)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors, 
                                status=status.HTTP_400_BAD_REQUEST)
	elif request.method == 'DELETE':
		sensor.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def Data_post(request):
	"""
	Post new Temperature data
        	
        """
	if request.method == 'POST':
		serializer = DataSerializer(data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, 
                                status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, 
                                status=status.HTTP_400_BAD_REQUEST)

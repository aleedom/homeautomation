from rest_framework import serializers

from main.models import *


class SensorSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Sensor
                fields = ('serial')

class DataSerializer(serializers.ModelSerializer):

	class Meta:
		 model = Data
		 fields = ('room_id','data','time','data_type')

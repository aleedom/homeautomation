from rest_framework import serializers

from main.models import *


class SensorSerializer(serializers.ModelSerializer):
        room_id = serializers.PrimaryKeyRelatedField(allow_null=True, read_only=True)
	class Meta:
		model = Sensor
                fields = ('serial','room_id',)

class DataSerializer(serializers.ModelSerializer):

	class Meta:
		 model = Data
		 fields = ('room_id','data','time','data_type')

from rest_framework import serializers

from main.models import Tsensor,Temperature


class TsensorSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Tsensor

class TemperatureSerializer(serializers.ModelSerializer):

	class Meta:
		 model = Temperature
		 fields = ('temperature', 'serial', 'timestamp')

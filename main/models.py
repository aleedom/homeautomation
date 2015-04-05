from django.db import models

	
class Room(models.Model):
	name = models.CharField(max_length=50,unique=True)
        #historical high and low temps
        temperature_high = models.OneToOneField('Data',blank=True ,null=True, default=None, related_name='+')
        temperature_low = models.OneToOneField('Data',blank=True, null=True, default=None, related_name='+')
        #current data
        temperature_current = models.OneToOneField('Data',blank=True, null=True, default=None, related_name='+')
        humidity_current = models.OneToOneField('Data', blank=True, null=True, default=None, related_name='+')
        vent_state = models.IntegerField(null=True,default=None)
        def _unicode__(self):
            return self.name

class Sensor(models.Model):
	#serial number of the xbee which the actual sensor is attached to
        serial = models.CharField(max_length=16,primary_key=True)
        room_id = models.ForeignKey('Room',
                null=True,
                blank=True,
                default=None,
                on_delete=models.SET_NULL)
        def __unicode__(self):
            return self.serial

class Data(models.Model):
	room_id = models.ForeignKey('Room')
	data = models.DecimalField(max_digits=6,decimal_places=3)
	time = models.DateTimeField()
        #data can be temperature or humidty or other 1 = temperature 2 = humidity, others ahve not been created yet
        data_type = models.IntegerField(null=True, default=1)

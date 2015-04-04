from django.db import models

	
class Room(models.Model):
	name = models.CharField(max_length=50)
        #historical high and low temps
        temperature_high = models.OneToOneField('Temperature',blank=True ,null=True, default=None, related_name='+')
        temperature_low = models.OneToOneField('Temperature',blank=True, null=True, default=None, related_name='+')
        #current temperature
        temperature_current = models.OneToOneField('Temperature',blank=True, null=True, default=None, related_name='+')
        
        sensor = models.ForeignKey('Tsensor',blank=True, null=True, default=None)
        def _unicode__(self):
            return self.name

class Tsensor(models.Model):
	serial = models.CharField(max_length=14,primary_key=True)
        
        def __unicode__(self):
            return self.serial

class Temperature(models.Model):
	serial = models.ForeignKey('Tsensor')
	temperature = models.DecimalField(max_digits=6,decimal_places=3)
	timestamp = models.DateTimeField()

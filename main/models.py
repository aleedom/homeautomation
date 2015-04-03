from django.db import models

class Room(models.Model):
	name = models.CharField(max_length=50)
        
        #historical high and low temps
        temperature_high = models.ForeignKey(Temperature, blank=True, default=blank)
        temperature_low = models.ForeignKey(Temperature, blank=True, default=blank)

        #current temperature
        temperature_current = models.ForeignKey(Temperature, blank=True, default=blank)

class Tsensor(models.Model):
	serial = models.CharField(max_length=14,primary_key=True)
        room = models.ForeignKey(Room, blank=True, default=blank)

class Temperature(models.Model):
	serial = models.ForeignKey(Tsensor)
	temperature = models.DecimalField(max_digits=6,decimal_places=3)
	timestamp = models.DateTimeField()
	

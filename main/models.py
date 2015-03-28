from django.db import models

class Room(models.Model):
	name = models.CharField(max_length=50)

class Tsensor(models.Model):
	serial = models.CharField(max_length=15,primary_key=True)
	active = models.BooleanField(default=True)
class Temperature(models.Model):
	serial = models.ForeignKey(Tsensor)
	temperature = models.DecimalField(max_digits=6,decimal_places=3)
	timestamp = models.DateTimeField()
	

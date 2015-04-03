from django.db import models

class Room(models.Model):
	name = models.CharField(max_length=50)

class Tsensor(models.Model):
	serial = models.CharField(max_length=14,primary_key=True)
class Temperature(models.Model):
	serial = models.ForeignKey(Tsensor)
	temperature = models.DecimalField(max_digits=6,decimal_places=3)
	timestamp = models.DateTimeField()
	

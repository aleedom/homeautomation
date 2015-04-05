from django import forms
from django.forms import ModelForm
from main.models import *

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ('name',)

class SensorForm(ModelForm):
    class Meta:
        model = Sensor
        fields = ('room_id',)


from django import forms
from django.forms import ModelForm
from main.models import *
"""
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ('name',)
"""
class RoomForm(forms.Form):
    name = forms.CharField(
            max_length=50)
    sensor_id = forms.ModelChoiceField(
            queryset=Sensor.objects.filter(room_id=None),
            empty_label="No Sensor",
            required=False,
            )

from django import forms
from django.forms import ModelForm
from main.models import *
"""
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ('name',)
"""
class RoomForm(forms.ModelForm):
    sensor_id = forms.ModelChoiceField(
            queryset=Sensor.objects.filter(room_id=None),
            empty_label="No Sensor",
            required=False,
            )
    def save(self, commit=True):
        instance = super(RoomForm, self).save(commit=True)
        sensor = Sensor.objects.get(serial=self.cleaned_data['sensor_id'])
        sensor.room_id = instance
        sensor.save()
        return instance

    class Meta:
        model = Room
        fields = ('name',)


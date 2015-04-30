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
    class Meta:
        model = Room
        fields = ('name',)

    #def save(self, commit=True):
    #    m = super(RoomForm, self).save(commit=True)
        #print(m.name, m.id)

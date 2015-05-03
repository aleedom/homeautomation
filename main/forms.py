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
            queryset=Sensor.objects.all(),
            empty_label="No Sensor",
            required=False,
            )
    def save(self, commit=True):
        """overiding save so that we can create/update sensor relationships"""

        #first need to create the room so we can reference it
        instance = super(RoomForm, self).save(commit=True)

        #need to get both old sensor(in the case we are updating) and new sensor
        try:
            #try and get old sensor
            old_sensor = Sensor.objects.get(room_id=instance)
        except:
            old_sensor = False

        try:
            #try to get the new sensor
            s_id = self.cleaned_data['sensor_id'].split(" ")[0]
            print("s_id: " + s_id)
            new_sensor = Sensor.objects.get(serial=self.cleaned_data['sensor_id'])
        except:
            new_sensor = False
            #selected sensor was null
        if not old_sensor and not new_sensor:
            #sensor associated with room is going from NULL to NULL
            print("Old: Nothing, New:Nothing")
            pass
        elif not old_sensor and new_sensor:
            #sensor associated with room is going from NULL to a sensor
            #no old sensor to update, only need to update new_sensor
            print("Old: Nothing, New:Nothing")
            new_sensor.room_id = instance
            new_sensor.save()
        elif old_sensor and not new_sensor:
            #sensor associated with room is going from something to NULL
            #reset old_sensor to null
            print("Old: Something, New:Nothing")
            old_sensor.room_id = None
            old_sensor.save()
        elif old_sensor and new_sensor and not(old_sensor == new_sensor):
            #sensor associated with room is changing from one sensor to another
            #need to reset old to NULL
            print("Old: Something, New:Something")
            old_sensor.room_id = None
            old_sensor.save()
            #also need to set new to the room instance
            new_sensor.room_id = instance
            new_sensor.save()
        return instance

    class Meta:
        model = Room
        fields = ('name',)


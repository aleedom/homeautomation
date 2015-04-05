from django import forms
from django.forms import ModelForm
from main.models import *
"""
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ('name',)
"""
class RoomForm(ModelForm):
    name = forms.CharField(max_length=50)
    sensor_id = forms.ModelChoiceField(empty_label="(Nothing"), to_field_name="serial")

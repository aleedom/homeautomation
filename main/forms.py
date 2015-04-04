from django import forms
from django.forms import ModelForm
from main.models import *

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ('name', 'sensor',)

from django.shortcuts import * 
from django.template import RequestContext
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse

from main.models import * 
from main.forms import *

class RoomNavMixin(object):
    """Adds a list of the created rooms to the context"""
    def get_context_data(self, **kwargs):
        context = super(RoomNavMixin, self).get_context_data(**kwargs)
        context['room_list'] = Room.objects.all().order_by('name')
        return context


class RoomIndex(RoomNavMixin, TemplateView):
    """Home Page, displays nav menue to go to different rooms and graphs of all"""
    template_name="main/room_index.html"


class RoomDetail(RoomNavMixin, DetailView):
    """Displays individual details of a singl room with a graph of only that rooms current sensor"""
    model = Room
    context_object_name = "current_room"
    def get_context_data(self,**kwargs):
        context = super(RoomDetail, self).get_context_data(**kwargs)
        try:
            sensor = Sensor.objects.get(room_id=self.kwargs['pk'])
            context['sensor_id'] = sensor.serial
        except:
            context['sensor_id'] = 'None'
        return context


class RoomCreate(RoomNavMixin, CreateView):
    """Displays a form which allows the user to create a new room"""
    form_class = RoomForm
    template_name = "main/room_create.html"


class RoomUpdate(RoomNavMixin, UpdateView):
    model = Room
    form_class = RoomForm
    template_name = "main/room_update.html"


class RoomDelete(RoomNavMixin, DeleteView):
    model = Room
    success_url = "/"
    template_name = "main/room_delete.html"
    def post(self, request, *args, **kwargs):
        if "Cancel" in request.POST:
            url = "/"
            return HttpResponseRedirect(url)
        else:
            return super(RoomDelete, self).post(request, *args, **kwargs)

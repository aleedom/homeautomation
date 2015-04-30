from django.shortcuts import * 
from django.template import RequestContext
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from main.models import * 
from main.forms import *

class RoomNavMixin(object):
    """Adds a list of the created rooms to the context"""
    def get_context_data(self, **kwargs):
        context = super(RoomNavMixin, self).get_context_data(**kwargs)
        context['room_list'] = Room.objects.all()
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
    success_url = "/"
    template_name = "main/room_create.html"


class RoomUpdate(RoomNavMixin, UpdateView):
    model = Room
    form_class = RoomForm
    success_url = "/"
    template_name = "main/room_update.html"


def room_modify(request,id):
    room_instance = get_object_or_404(Room, id=id)
    form = RoomForm(request.POST or None)
    #if request.POST:
    #    form.fields['name'] = request.POST['name']
    #else:
    #    form.fields['name'] = instance.name

    if form.is_valid():
        #first check ot see if the serial was changed
        print("old,new",form.fields['sensor_id'],room_instance.serial)
        if form.fields['sensor_id'] ==  room_instance.serial:
            print("Sensor did not change")
        else:
            print("Sensor changed")
        
        room_instance.name = form.name
        #room_instance.save()
        if request.POST['sensor_id'] == None:
            return redirect('/rooms')
        else:
            sensor = Sensor.objects.get(serial=request.POST['sensor_id'])
            sensor.room_id = new_
        #form.save()
        return redirect('main.views.room_detail',id)

    return render_to_response('main/room_modify.html',
            {'form':form, 'id':id, 'prev_name':room_instance.name},
        context_instance=RequestContext(request))

def room_delete(request,id):
    room_instance = get_object_or_404(Room, id=id)
    try:
        sensor = Sensor.objects.get(room_id=room_instance)
        if sensor:
            sensor.room_id = None
    except:
        print("no sensor associated with that room")
    room_instance.delete()
    
    return redirect('main.views.room_list')


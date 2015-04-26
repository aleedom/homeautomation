from django.shortcuts import * 
from django.template import RequestContext
from django.http import HttpResponse

from main.models import * 
from main.forms import *


def index(request):
    context = {'name':'Andy'}
    return render(request, 'main/index.html',context) 

def room_detail(request,id):
        room = get_object_or_404(Room,id=id)
        context = {}
        context['room_name'] = room.name
        context['id'] = id
        if room.temperature_high:
            context['temp_high'] = room.temperature_high.data
            context['temp_high_time'] = room.temperature_high.time
        else:
            context['temp_high'] = "Highest temperature not available"

        if room.temperature_low:
            context['temp_low'] = room.temperature_low.data
            context['temp_low_time'] = room.temperature_low.time
        else:
            context['temp_low'] = "Lowest temperature not available"

        if room.temperature_current:
            context['temp_current'] = room.temperature_current.data
            context['temp_current_time'] = room.temperature_current.time
        else:
            context['temp_current'] = "Current temperature not available"
        try:
            sensor = Sensor.objects.get(room_id=room)
        except:
            sensor = False
            #print("No sensor associated with this room!")
        if sensor:
            context['sensor_id'] = sensor.serial
        else:
            context['sensor_id'] = "No temperature Sensor associated with this room"
        return render(request, 'main/room_detail.html',context)

class RoomCreate(CreateView):
    form_class = RoomForm
    success_url = "/rooms"
    template_name = "main/room_create.html"
    def form_valid(self, form):
        print("Form is valid")
        print(request.POST['name'],request.POST['sensor_id'])
        return super(RoomCreateView, self).form_valid(form)

"""
def room_create(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        print(request.POST['name'],request.POST['sensor_id'])
        if(form.is_valid()):
            new_room = Room(
                    name=request.POST['name'],
                    temperature_high=None, 
                    temperature_low=None, 
                    temperature_current=None,
                    humidity_current = None,
                    vent_state=None
                    )
            new_room.save()
            if request.POST['sensor_id'] == None:
                return redirect('/rooms') 
            else:
                sensor = Sensor.objects.get(serial=request.POST['sensor_id'])
                sensor.room_id = new_room
                sensor.save()
                return redirect('/rooms')
    else:
        form = RoomForm()
        return render_to_response('main/room_create.html',
                {'form':form},
                context_instance=RequestContext(request))
"""
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


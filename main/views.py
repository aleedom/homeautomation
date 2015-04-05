from django.shortcuts import * 
from django.template import RequestContext
from django.http import HttpResponse

from main.models import * 
from main.forms import *


def index(request):
    context = {'name':'Andy'}
    return render(request, 'main/index.html',context) 

def room_list(request):
    room_list = Room.objects.all()
    context = {'room_list': room_list}
    return render(request, 'main/room_list.html', context)

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
        
        sensor = Sensor.objects.get(room_id=id)
        if sensor:
            context['sensor_id'] = sensor.serial
        else:
            context['sensor_id'] = "No temperature Sensor associated with this room"
        return render(request, 'main/room_detail.html',context)

def room_create(request):
    if request.method == "POST":
        
        form = RoomForm(request.POST)
        if(form.is_valid()):
            form.save()
            print(request.POST['name'])
            return redirect('/rooms')
    else:
        form = RoomForm()
        return render_to_response('main/room_create.html',
                {'form':form},
                context_instance=RequestContext(request))

def room_modify(request,id):
    instance = get_object_or_404(Room, id=id)
    form = RoomForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('main.views.room_detail',id)

    return render_to_response('main/room_modify.html',
            {'form':form, 'id':id},
        context_instance=RequestContext(request))

def room_delete(request,id):
    instance = get_object_or_404(Room, id=id).delete()
    return redirect('main.views.room_list')

#def sensor_list(request):
#	sensor_list = Sensor.objects.all()
#	context = {'sensor_list': sensor_list}
#	return render(request, 'main/sensor_list.html', context)

#def sensor_detail(request, serial):
#	temp_list = Data.objects.filter(serial=serial)
#	context = {'temp_list':temp_list}
#	return render(request, 'main/sensor_detail.html', context)

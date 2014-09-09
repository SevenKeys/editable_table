from django.shortcuts import render
from models import User,Room
from forms import RoomForm
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponse, Http404

def show_rooms(request):
    list_rooms = Room.objects.all()
    return render(request,'show_rooms.html',
        {'list_rooms':list_rooms})

def add_room(request):
    list_rooms = Room.objects.order_by('number')
    if request.POST:
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')
    else:
        form = RoomForm()
    args={}
    args.update(csrf(request))
    args['form']=form
    args['list_rooms'] = list_rooms
    return render(request,'add_room.html',args)

def success(request):
    return render(request,'success.html')

def change_data(request, room_id):
    try:
        room = Room.objects.get(id=room_id)
    except Room.DoesNotExists:
        raise Http404
    if request.method == 'POST':
        old_data = request.POST['old_data']
        new_data = request.POST['new_data']
        if room.id == int(room_id):
            if room.number == int(old_data):
                room.number = int(new_data)
            elif room.department == old_data:
                room.department = new_data
            elif room.capacity == int(old_data):
                room.capacity = int(new_data)
            room.save()
        return HttpResponse("It works!")
    return render(request,'show_rooms.html',{'data':new_data})
                        

def show_users(request):
    list_users = User.objects.order_by('date_admit')
    return render(request,'show_users.html',
        {'list_users':list_users})

def add_user(request):
    list_users=User.objects.order_by('date_admit')
    if request.POST:
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')
    else:
        form=UserForm()
    args={}
    args.update(csrf(request))
    args['form']=form
    args['list_users']=list_users
    return render(request,'add_user.html',args)




        



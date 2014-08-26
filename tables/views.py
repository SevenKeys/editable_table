from django.shortcuts import render
from models import User,Room
#from django.forms import UserForm
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect,HttpResponse

def show_rooms(request):
    list_rooms = Room.objects.all()
    return render(request,'show_rooms.html',
        {'list_rooms':list_rooms})

def add_room(request):
    list_rooms = Room.objects.order_by('number')
    if request.POST:
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')
    else:
        form=UserForm()
    args={}
    args.update(csrf(request))
    args['form']=form
    args['list_rooms']=list_users
    return render(request,'add_room.html',args)

def change_data(request):
    rooms = Room.objects.all()
    if request.method == 'POST':
        return HttpResponse("It works!")
        _id = request.POST['_id']
        old_data = request.POST['old_data']
        new_data = request.POST['new_data']
        for room in rooms:
            if room.id == _id:
                if room.number == old.data:
                    room.number = new_data
                elif room.department == old_data:
                    room.department = new_data
                elif room.capacity == old_data:
                    room.capacity = new_data
                room.save()
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

def success(request):
    list_users=User.objects.order_by('date_admit')
    return render(request,'success.html',
                  {'list_users':list_users})


        



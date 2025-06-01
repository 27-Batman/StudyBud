from django.shortcuts import render

rooms = [
    {'id':1, 'name':"Hello There"},
    {'id':2, 'name':"How are you"},
    {'id':3, 'name':"Let code together"}
]

def home(request):
    return render(request, 'base/home.html', {'rooms':rooms})

def room(request, pk):
    room = 0
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}

    return render(request, 'base/room.html', context)
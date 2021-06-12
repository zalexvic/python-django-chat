from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Room, Message
from .forms import (
    CreateRoomForm,
    EditProfileForm,
    EnterRoomForm,
    JoinRoomForm,
    EditRoomForm
)


# Create your views here.
def index(request):
    user = request.user
    context = {}

    if user.is_authenticated:
        user_rooms = user.all_rooms.all()
        rooms_per_page = 15

        paginator = Paginator(user_rooms, rooms_per_page)

        page_num = request.GET.get('page', 1)
        page = paginator.page(page_num)

        context = {'page': page}

    if request.method == "POST":
        if request.POST.get('leave') is not None:
            room_id = int(request.POST.get('leave'))
            room = Room.objects.get(id=room_id)

            user = request.user
            room.users.remove(user)
        elif request.POST.get('delete') is not None:
            room_id = int(request.POST.get('delete'))
            room = Room.objects.get(id=room_id)

            room.delete()
        elif request.POST.get('edit') is not None:
            room_id = request.POST.get('edit')
            return redirect('/chat/edit-room/' + room_id)

    return render(request, 'chat/index.html', context)


def room(request, room_id):
    room = Room.objects.get(id=room_id)
    room_name = room.name

    user = request.user

    if user not in room.users.all():
        return redirect('/chat/enter-room/' + str(room_id))

    user_id = user.id
    handle = user.profile.handle
    profile_pic = user.profile.profile_pic.url

    messages = Message.objects.filter(room_id=room_id)[0:25:-1]

    return render(request, 'chat/room.html', {
        "room_id": room_id,
        "room_name": room_name,
        "handle": handle,
        "profile_pic": profile_pic,
        "user_id": user_id,
        'messages': messages
    })


def create_room(request):
    if request.method == "POST":
        form = CreateRoomForm(request.POST)
        user = request.user
        if form.is_valid():
            room_name = form.cleaned_data['room_name']
            room_password = form.cleaned_data['room_password']

            room = Room.objects.create(creator=user, name=room_name, password=room_password)

            room.users.add(user)
            room_id = room.id
            return redirect('/chat/' + str(room_id))
    else:
        form = CreateRoomForm()
    return render(request, 'chat/create-room.html', {'form': form})


def edit_room(request, room_id):
    if request.method == "POST":
        form = EditRoomForm(request.POST)
        room = Room.objects.get(id=room_id)
        if form.is_valid():
            if form.cleaned_data['room_name']:
                room.name = form.cleaned_data['room_name']
                room.save()
            if form.cleaned_data['room_password']:
                room.password = form.cleaned_data['room_password']
                room.save()
        return redirect('/')
    else:
        form = EditRoomForm()
    return render(request, 'chat/edit-room.html', {'form':form})


def enter_room(request, room_id):
    if request.method == "POST":
        form = EnterRoomForm(request.POST)
        room = Room.objects.get(id=room_id)
        user = request.user
        if form.is_valid() and form.cleaned_data['password'] == room.password:
            room.users.add(user)
            return redirect('/chat/' + str(room_id))
    else:
        form = EnterRoomForm()
    return render(request, 'chat/enter-room.html', {'form': form})


def join_room(request):
    if request.method == "POST":
        form = JoinRoomForm(request.POST)
        if form.is_valid():
            return redirect('/chat/enter-room/' + str(form.cleaned_data['room_id']))
    else:
        form = JoinRoomForm()
    return render(request, 'chat/join-room.html', {'form': form})


def all_rooms(request):
    user = request.user
    context = {}
    if user.is_authenticated:
        rooms = Room.objects.all()
        rooms_per_page = 15

        paginator = Paginator(rooms, rooms_per_page)

        page_num = request.GET.get('page', 1)
        page = paginator.page(page_num)

        context = {'page': page}
    return render(request, 'chat/all-rooms.html', context)


def profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = request.user.profile

            if form.cleaned_data['profile_pic']:
                profile.profile_pic = form.cleaned_data['profile_pic']
                profile.save()

            if form.cleaned_data['handle']:
                profile.handle = form.cleaned_data['handle']
                profile.save()
    else:
        form = EditProfileForm()
    return render(request, 'chat/profile.html', {'form': form})


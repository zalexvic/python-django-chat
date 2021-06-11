from django.shortcuts import render, redirect
from .models import Room
from .forms import CreateRoomForm, EditProfileForm


# Create your views here.
def index(request):
    return render(request, 'chat/index.html')


def room(request, room_id):
    return render(request, 'chat/room.html', {
        "room_id": room_id,
    })


def create_room(request):
    if request.method == "POST":
        form = CreateRoomForm(request.POST)
        room_id = None
        if form.is_valid():
            room_name = form.cleaned_data['room_name']
            room_password = form.cleaned_data['room_password']
            request.user.room_set.create(name=room_name, password=room_password)
            room_id = Room.objects.latest('id').id
        if room_id is None:
            return redirect('/')
        else:
            return redirect('/chat/' + str(room_id))
    else:
        form = CreateRoomForm()
    return render(request, 'chat/create-room.html', {'form': form})


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


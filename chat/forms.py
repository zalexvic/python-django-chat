from django import forms
from .models import Profile, Room


class CreateRoomForm(forms.Form):
    room_name = forms.CharField(max_length=100, required=True)
    room_password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput())

    class Meta:
        model = forms.ModelForm
        fields = ['room_name', 'room_password']


class EditProfileForm(forms.Form):
    handle = forms.CharField(max_length=30, required=False)
    profile_pic = forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ['handle', 'profile_pic']


class EnterRoomForm(forms.Form):
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput())

    class Meta:
        model = Room
        fields = ['password']


class JoinRoomForm(forms.Form):
    room_id = forms.IntegerField(required=True)


class EditRoomForm(forms.Form):
    room_name = forms.CharField(max_length=200, required=False)
    room_password = forms.CharField(max_length=50, required=False, widget=forms.PasswordInput())

    class Meta:
        model = Room
        fields = ['room_name', 'room_password']
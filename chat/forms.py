from django import forms
from .models import Profile


class CreateRoomForm(forms.Form):
    room_name = forms.CharField(max_length=100, required=True)
    room_password = forms.CharField(max_length=50, required=True)

    class Meta:
        model = forms.ModelForm
        fields = ['room_name', 'room_password']


class EditProfileForm(forms.Form):
    handle = forms.CharField(max_length=30, required=False)
    profile_pic = forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ['handle', 'profile_pic']
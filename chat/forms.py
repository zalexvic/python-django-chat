from django import forms


class CreateRoomForm(forms.Form):
    room_name = forms.CharField(max_length=100, required=True)
    room_password = forms.CharField(max_length=50, required=True)

    class Meta:
        model = forms.ModelForm
        fields = ['room_name', 'room_password']
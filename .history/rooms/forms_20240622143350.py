from django.forms import ModelForm
from .models import Room,Booking

class room_form(ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    class Meta:
        model=Room
        fields="__all__"
        exclude=["user","hotels"]










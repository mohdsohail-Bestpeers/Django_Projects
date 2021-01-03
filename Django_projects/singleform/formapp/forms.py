from django import forms
from . models import User, Event, Address, event_photo
#from . models import Event


class user_form(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'


class event_form(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'


class address_form(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

    
class event_photo_form(forms.ModelForm):
    class Meta:
        model = event_photo
        fields = '__all__'

from django import forms
from . models import User, myprofile
'''class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))'''


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class myprofileForm(forms.ModelForm):
    class Meta:
        model = myprofile
        fields = '__all__'
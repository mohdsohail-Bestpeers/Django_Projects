from django import forms  
from .models import User
  
  

class SignupForm(forms.ModelForm):  
    class Meta:  
        model = User  
        fields = "__all__"
       

   # password = forms.CharField(widget=forms.PasswordInput)
 
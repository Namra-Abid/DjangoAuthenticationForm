from django.forms  import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import  forms 


#Creating Custom Class and inherit properties of UserCreatonForm

class Custom_UserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields= ['username','email','password1','password2']


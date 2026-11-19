from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
 


class customRegistrationForm(UserCreationForm): # ready made model form main se ak new form create karo jisaka name TaskForm h
    email = forms.EmailField(required=True)
    class Meta: # class Meta main hum model ka name or fields ka name define karte h
        model = User
        fields = ['username', 'email']
# after changes need to update views.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):   #dopełnienie UserCreationForm o nowe pozycje
    email = forms.EmailField(required=True) #domyślnie required jest true

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True) #domyślnie required jest true

    class Meta:
        model = User
        fields = ['email']

class ProfileUpdateForm(forms.ModelForm):
   class Meta:
       model = Profile
       fields = []

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

# Custom registration form for the custom user model
class CustomUserCreationForm(UserCreationForm):
    date_of_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    profile_photo = forms.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'date_of_birth', 'profile_photo', 'password1', 'password2']

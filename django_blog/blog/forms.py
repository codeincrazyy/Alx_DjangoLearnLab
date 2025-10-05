from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .models import Post

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'image']
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
       
        fields = ['title', 'content']

    
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter post title', 'class': 'form-input'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write your post...', 'class': 'form-textarea'}),
        }

from django import forms
from django.forms import ModelForm, TextInput, ImageField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Image, Comments


class SignUpForm(UserCreationForm):
    """
    creating signupform
    UserCreationForm passed as a parameter of signup form making SignUpForm extend UserCreationForm
    """
    email = forms.CharField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['email']
        fields = ['avatar', 'Bio', 'location', 'phone_number']


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image', 'image_name', 'caption']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']

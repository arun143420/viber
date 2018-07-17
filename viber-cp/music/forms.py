from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from music.models import Profile
from django.utils.translation import gettext as _



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=30)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']




class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = [ 'phone', 'address']
        labels ={'phone':'mob', 'user':'client'}


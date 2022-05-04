# authentication/forms.py
from django import forms
from .models import *

# class ImageForm(forms.ModelForm):

#   time = forms.DateTimeField()

# 	class Meta:
#       model = PhotoData
# 		fields = ['photo', 'time', 'userId']


class ImageForm(forms.ModelForm):
    time = forms.DateTimeField(required=True)
    class Meta:
        model = PhotoData
        fields = ['photo', 'time', 'userId']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from django import forms
from account.models import Profile

class MemberChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = get_user_model()
        fields = ['memberName', 'phoneNumber', 'gender', 'email', 'address']

class ProfileForm(forms.ModelForm):
    model = Profile
    fields = ['nickname', 'introduction', 'photo']

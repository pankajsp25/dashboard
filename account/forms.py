from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from account.models import Profile

User = get_user_model()


class UserRegistrationForm(UserCreationForm):

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['username'].label = 'User name'

    class Meta(UserCreationForm.Meta):
        fields = ('first_name', 'last_name', 'email', 'username',)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'




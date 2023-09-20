from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth import get_user_model
from django import forms
from django.utils.translation import gettext_lazy as _

from .models import *
from django.forms import ModelForm, TextInput, Textarea, Select, FileInput, EmailInput, NumberInput
 
User = get_user_model()

class UserCreationForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email", 'class': 'form-control'}),
    )
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta(UserCreationForm.Meta):
        model =  User
        fields = ("username", "email")


class EditUserAccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ["img"]

        widgets = {
            "img": FileInput(attrs={
                "class": "form-control",
                "type": "file",
                "id": "formFile",
            }),
        }


class PassworduserForm(ModelForm):
    class Meta:
        model = PasswordUser
        fields = ["url", "login", "password",
                  "detail"]
        
        widgets = {
            "url": TextInput(attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "https://apple.com",
                "aria-label": "url",
                "aria-describedby": "basic-addon1",
                "id": "formUrl",
            }),
            "login": TextInput(attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "Tim Сookies",
                "aria-label": "login",
                "aria-describedby": "basic-addon1",
                "id": "formLogin",
            }),
            "password": TextInput(attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "appl3C00lxD",
                "aria-label": "password",
                "aria-describedby": "basic-addon1",
                "id": "formPassword",
            }),
            "detail": Textarea(attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "It's my main account for apple... 🍏",
                "aria-label": "detail",
                "aria-describedby": "basic-addon1",
                "id": "formDetail",
            }),
        }
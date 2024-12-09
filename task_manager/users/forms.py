from django import forms
from .models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(forms.ModelForm):
    first_name = forms.CharField(
        label=_('Имя'),
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': _('Имя')})
    )

    last_name = forms.CharField(
        label=_('Фамилия'),
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': _('Фамилия')})
    )

    username = forms.CharField(
        label=_('Имя пользователя'),
        help_text=_('Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.'),
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': _('Имя пользователя')})
    )

    password1 = forms.CharField(
        min_length=3,
        label=_('Пароль'),
        help_text=_('Ваш пароль должен содержать как минимум 3 символа.'),
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': _('Пароль')})
    )

    password2 = forms.CharField(
        min_length=3,
        label=_('Подтверждение пароля'),
        help_text=_('Для подтверждения введите, пожалуйста, пароль ещё раз.'),
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': _('Подтверждение пароля')})
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']


class LoginForm(forms.ModelForm):
    username = forms.CharField(
        label=_('Имя пользователя'),
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': _('Имя пользователя')})
    )

    password = forms.CharField(
        min_length=3,
        label=_('Пароль'),
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': _('Пароль')})
    )

    class Meta:
        model = User
        fields = ['username', 'password']

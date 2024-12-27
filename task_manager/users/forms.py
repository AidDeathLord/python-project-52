from django import forms
from .models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']


class UserForm(UserCreationForm):
    first_name = forms.CharField(
        label=_('Имя'),
        max_length=150
    )
    last_name = forms.CharField(
        label=_('Фамилия'),
        max_length=150
    )

    password1 = forms.CharField(
        label=_('Пароль'),
        help_text=_('Ваш пароль должен содержать как минимум 3 символа.'),
        widget=forms.PasswordInput(attrs={'placeholder': _('Пароль')})
    )

    password2 = forms.CharField(
        label=_('Подтверждение пароля'),
        help_text=_('Для подтверждения введите, пожалуйста, пароль ещё раз.'),
        widget=forms.PasswordInput(attrs={'placeholder': _('Подтверждение пароля')})
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']


class UserUpdateForm(UserChangeForm):

    password1 = forms.CharField(
        label=_('Пароль'),
        help_text=_('Ваш пароль должен содержать как минимум 3 символа.'),
        widget=forms.PasswordInput(attrs={'placeholder': _('Пароль')})
    )

    password2 = forms.CharField(
        label=_('Подтверждение пароля'),
        help_text=_('Для подтверждения введите, пожалуйста, пароль ещё раз.'),
        widget=forms.PasswordInput(attrs={'placeholder': _('Подтверждение пароля')})
    )

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        del self.fields['password']

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')

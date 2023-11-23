from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """Форма создания переопределённого пользователя для админ панели"""
    class Meta:
        model = CustomUser
        fields = ('username', 'email',)


class CustomUserChangeForm(UserChangeForm):
    """Форма редактирования переопределённого пользователя для админ панели"""
    class Meta:
        model = CustomUser
        fields = ('username', 'email',)

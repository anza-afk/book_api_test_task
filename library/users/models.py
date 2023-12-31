from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from users.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Модель переопределённого пльзователя.
    """
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_(
            ('Required. 150 characters or fewer. '
             'Letters, digits and @/./+/-/_ only.')
        ),
        validators=[UnicodeUsernameValidator()],
        error_messages={
            'unique': _('A user with that username already exists.'),
        },
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.username}, {self.email}'

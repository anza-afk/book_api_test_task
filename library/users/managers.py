from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.db.models import Model


class CustomUserManager(BaseUserManager):
    """
    Менеджер создания переопределённог опользователя.
    """
    def create_user(
            self,
            username: str,
            email: str,
            password: str,
            **extra_fields
    ) -> Model:
        """
        Создаёт и сохраняет пользователя
        с именем, электронной почтой и паролем.
        """
        if not username:
            raise ValueError(_("The Username must be set"))
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        extra_fields.setdefault("is_active", True)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
            self,
            username: str,
            email: str,
            password: str,
            **extra_fields
    ) -> Model:
        """
        Создаёт и сохраняет суперпользователя
        с именем, электронной почтой и паролем.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(
            email=email,
            username=username,
            password=password,
            **extra_fields
        )

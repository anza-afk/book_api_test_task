from celery import shared_task

from django.conf import settings
from django.core.mail import send_mail


@shared_task()
def send_hello_email_task(username, email):

    """Sends an email when neww user regitered."""
    send_mail(
        subject="Успешная регистрация.",
        message=f"Перивет, {username}\nСпасибо за регистрацию!",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False,
    )

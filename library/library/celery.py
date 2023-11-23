import os

from celery import Celery


# Настройка Celery из главного файла настроек проекта.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "library.settings")
app = Celery("library")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

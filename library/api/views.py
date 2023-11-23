from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.serializers import BookSerializer, CustomUserSerializer
from books.models import Book
from users.models import CustomUser
from users.tasks import send_hello_email_task


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [
        permissions.AllowAny
    ]


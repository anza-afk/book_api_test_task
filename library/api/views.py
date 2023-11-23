from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet

from api.serializers import BookSerializer, CustomUserSerializer
from books.models import Book
from users.models import CustomUser
from users.tasks import send_hello_email_task


class BookViewSet(ModelViewSet):
    """Эндпоинт для просмотра, создания, удаления книг"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class CreateUserView(CreateAPIView):
    """Эндпоинт для регистрации переопределённого пользователя"""
    model = CustomUser
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CustomUserSerializer

    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        print(user.email)
        send_hello_email_task.delay(
            username=user.username,
            email=user.email,
        )
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

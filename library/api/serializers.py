from rest_framework import serializers

from books.models import Book
from users.models import CustomUser


class BookSerializer(serializers.ModelSerializer):
    """Сериализатор модели книги"""
    class Meta:
        model = Book
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    """Сериализатор модели переопределённог опользователя."""
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password',)

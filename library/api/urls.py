from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import BookViewSet

router = DefaultRouter()

router.register('books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

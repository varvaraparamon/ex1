from rest_framework import generics, permissions
from drf_spectacular.utils import extend_schema
from reviews.models import Reviews
from .serializers import ReviewSerializer


@extend_schema(tags=['Отзывы'], summary='Список / создание отзывов')
class ReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


@extend_schema(tags=['Отзывы'], summary='Детали / изменение / удаление отзыва')
class ReviewRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
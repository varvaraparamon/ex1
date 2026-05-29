from rest_framework import generics, permissions
from drf_spectacular.utils import extend_schema
from catalog.models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


@extend_schema(tags=['Категории'], summary='Список / создание категорий')
class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  


@extend_schema(tags=['Категории'], summary='Детали / изменение / удаление категории')
class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]  


@extend_schema(tags=['Товары'], summary='Список / создание товаров')
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


@extend_schema(tags=['Товары'], summary='Детали / изменение / удаление товара')
class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser]
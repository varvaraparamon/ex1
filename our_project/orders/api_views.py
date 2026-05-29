from rest_framework import generics, permissions
from drf_spectacular.utils import extend_schema
from orders.models import Order
from .serializers import OrderSerializer


@extend_schema(tags=['Заказы'], summary='Список / создание заказов')
class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


@extend_schema(tags=['Заказы'], summary='Детали / изменение / удаление заказа')
class OrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
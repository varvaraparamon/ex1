from rest_framework import serializers
from orders.models import Order, OrderItem
from catalog.models import Product
from django.contrib.auth.models import User


class OrderUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price']


class OrderItemSerializer(serializers.ModelSerializer):
    product = OrderProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'price', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    user = OrderUserSerializer(read_only=True)
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'created_at', 'is_paid', 'items']
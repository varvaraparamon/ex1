from rest_framework import serializers
from catalog.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class ProductShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'stock', 'is_available', 'category']
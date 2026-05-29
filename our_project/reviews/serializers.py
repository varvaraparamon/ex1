from rest_framework import serializers
from reviews.models import Reviews
from users.serializers import UserShortSerializer
from catalog.serializers import ProductShortSerializer


class ReviewSerializer(serializers.ModelSerializer):
    user = UserShortSerializer(read_only=True)
    product = ProductShortSerializer(read_only=True)

    class Meta:
        model = Reviews
        fields = ['id', 'text', 'rating', 'user', 'product']
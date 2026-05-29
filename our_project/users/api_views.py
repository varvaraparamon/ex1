from rest_framework import generics, permissions
from drf_spectacular.utils import extend_schema
from users.models import Profile
from .serializers import ProfileSerializer


@extend_schema(tags=['Профиль'], summary='Мой профиль (просмотр / изменение)')
class MyProfileRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return Profile.objects.get(user=self.request.user)
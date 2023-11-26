from rest_framework.viewsets import ModelViewSet

from .mixins import UserSearchMixin
from .models import User
from .serializers import UserDetailSerializer, UsersListSerializer


class UserViewSet(ModelViewSet, UserSearchMixin):
    serializer_class = UsersListSerializer
    detail_serializer_class = UserDetailSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()

    def get_queryset(self):
        return User.objects.all()



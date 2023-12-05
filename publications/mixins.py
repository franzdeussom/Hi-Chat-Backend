from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.serializers import UserListSerializer


class LikeViewSetMixin:
    @action(methods=['GET'], detail=True, permission_classes=[IsAuthenticated])
    def likes(self, request, *args, **kwargs):
        users = self.get_object().likes.all()
        return Response(UserListSerializer(users, many=True).data)

    @action(methods=['POST'], detail=True, permission_classes=[IsAuthenticated])
    def like(self, request, *args, **kwargs):
        self.get_object().likes.add(request.user)
        return Response()

    @action(methods=['POST'], detail=True, permission_classes=[IsAuthenticated])
    def unlike(self, request, *args, **kwargs):
        self.get_object().likes.remove(request.user)
        return Response()

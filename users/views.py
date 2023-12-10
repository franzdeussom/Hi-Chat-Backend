from rest_framework import status, exceptions
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from hichat.permissions import IsOwnerOrReadOnly
from publications.models import Publication
from publications.serializers import PublicationSerializer
from .mixins import UserSearchMixin
from .models import User
from .serializers import UserDetailSerializer, UserListSerializer


class UserViewSet(UserSearchMixin, ModelViewSet):
    serializer_class = UserDetailSerializer
    list_serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.action == "list":
            return self.list_serializer_class or super().get_serializer_class()
        return super().get_serializer_class()

    def get_queryset(self):
        return User.objects.all()

    @action(methods=["GET"], detail=True)
    def followers(self, request, *args, **kwargs):
        followers = UserListSerializer(self.get_object().followers.all(), many=True)
        return Response(followers.data, status=status.HTTP_200_OK)

    @action(methods=["GET"], detail=True)
    def followings(self, request, *args, **kwargs):
        followings = UserListSerializer(self.get_object().followings.all(), many=True)
        return Response(followings.data, status=status.HTTP_200_OK)

    @action(methods=["GET"], detail=True, url_path='followings/publications')
    def followings_pub(self, request, *args, **kwargs):
        publications = Publication.objects.filter(owner__in=self.get_object().followings.all(), public=True)
        data = PublicationSerializer(publications, many=True, context={"request": request}).data
        return Response(data, status=status.HTTP_200_OK)

    @action(methods=["POST"], detail=True, permission_classes=[IsAuthenticated])
    def follow(self, request, *args, **kwargs):
        self.get_object().followers.add(request.user)
        return Response()

    @action(methods=["POST"], detail=True, permission_classes=[IsAuthenticated])
    def unfollow(self, request, *args, **kwargs):
        self.get_object().followers.remove(request.user)
        return Response()

    @action(methods=["GET"], detail=True)
    def publications(self, request, *args, **kwargs):
        publications = Publication.objects.filter(owner=self.get_object(), public=True)
        data = PublicationSerializer(publications, many=True, context={"request": request}).data
        return Response(data, status=status.HTTP_200_OK)

    @action(methods=["GET"], detail=True)
    def boosted_publications(self, request, *args, **kwargs):
        raise exceptions.PermissionDenied
        # publications = Publication.objects.filter(owner=self.get_object(), public=True)
        # data = PublicationSerializer(publications, many=True, context={"request": request}).data
        # return Response(data, status=status.HTTP_200_OK)

    @action(methods=["GET"], detail=True)
    def user_followers_home(self, request, *args, **kwargs):
        raise exceptions.PermissionDenied
        # publications = Publication.objects.filter(owner=self.get_object(), public=True)
        # data = PublicationSerializer(publications, many=True, context={"request": request}).data
        # return Response(data, status=status.HTTP_200_OK)

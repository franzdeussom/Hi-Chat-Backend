from rest_framework.permissions import IsAuthenticated
from rest_framework_nested.viewsets import NestedViewSetMixin

from hichat.permissions import IsOwnerOrReadOnly
from hichat.viewsets import HichatModelViewSet
from .mixins import LikeViewSetMixin
from .models import Publication, Comment
from .serializers import PublicationSerializer, CommentSerializer


class PublicationViewSet(LikeViewSetMixin, HichatModelViewSet):
    serializer_class = PublicationSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    # parent_lookup_kwargs = {'user_pk': 'owner'}

    def get_queryset(self):
        if self.action in ('list',):
            return Publication.objects.filter(owner=self.request.user)
        return Publication.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentViewSet(NestedViewSetMixin, LikeViewSetMixin, HichatModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    parent_lookup_kwargs = {'publication_pk': 'publication'}

    def get_queryset(self):
        return Comment.objects.filter(publication=self.kwargs.get('publication_pk'))

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

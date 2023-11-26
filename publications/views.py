from rest_framework.viewsets import ModelViewSet

from .models import Publications
from .serializers import PublicationSerializer, PublicationDetailSerializer


class UserPublicationViewSet(ModelViewSet):
    serializer_class = PublicationSerializer
    detail_serializer_class = PublicationDetailSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()

    def get_queryset(self):
        return Publications.objects.all()


class PublicationViewSet(ModelViewSet):
    serializer_class = PublicationSerializer
    detail_serializer_class = PublicationDetailSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()

    def get_queryset(self):
        return Publications.objects.all()
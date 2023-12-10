from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_nested.viewsets import NestedViewSetMixin

from chat.models import Message
from chat.permissions import IsSenderOrReadOnly
from chat.serializers import MessageSerializer
from users.models import User


class MessageViewSet(NestedViewSetMixin, ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, IsSenderOrReadOnly]

    parent_lookup_kwargs = {'user_pk': 'sender'}

    def get_queryset(self):
        return Message.objects.filter(sender=self.kwargs['user_pk'])

    @action(methods=['GET'], detail=False, url_path='(?P<receiver>[0-9]+)')
    def to(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs.get('receiver'))
        messages = self.get_queryset().filter(receiver=user)
        return Response(self.get_serializer(messages, many=True).data)

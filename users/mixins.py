from rest_framework.decorators import action
from rest_framework.response import Response

from .models import User
from .serializers import UsersListSerializer


class UserSearchMixin:
    @action(methods=["GET"], detail=False)
    def search(self, request):
        last_name = request.GET.get('last_name', '')
        first_name = request.GET.get('first_name', '')
        queryset = User.objects.filter(last_name__icontains=last_name, first_name__icontains=first_name)
        return Response(UsersListSerializer(queryset, many=True).data)

    # TODO search with attribute

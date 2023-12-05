from django.http import HttpRequest, QueryDict
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import User
from .serializers import UserListSerializer


class UserSearchMixin:
    @action(methods=["GET"], detail=False)
    def search(self, request: HttpRequest):
        query = self._parse_query(request.GET)
        if len(query.keys()) == 0:
            return Response({
                "detail": "no search options provided if you want to fetch all users list consider this path "
                          "/api/users/"
            },
                status=status.HTTP_400_BAD_REQUEST)
        queryset = User.objects.filter(**query)
        return Response(UserListSerializer(queryset, many=True).data)

    def _parse_query(self, query_dict: QueryDict):
        fields = {
            'phone': 'iexact',
            'city': 'icontains',
            'country': 'icontains',
            'last_name': 'icontains',
            'first_name': 'icontains',
            'email': 'iexact',
            'gender': 'iexact',
            'age': 'exact'
        }
        query = {}
        for key in fields:
            if key in query_dict:
                query[f"{key}__{fields[key]}"] = query_dict.get(key)
        return query

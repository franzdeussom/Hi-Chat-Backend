from django.http import HttpRequest
from rest_framework import permissions

from users.models import User


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request: HttpRequest, view, obj):
        print('permission check on', obj)
        if request.method in permissions.SAFE_METHODS:
            return True
        if isinstance(obj, User):
            return obj == request.user
        return obj.owner == request.user

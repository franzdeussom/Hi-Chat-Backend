from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer


class UsersListSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "email", "profile", "account_type", "last_login", "is_active"]


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', "first_name", "last_name", "password", "email", "age",
                  "gender", "phone", "birthday", "country", "city", "profile",
                  "account_type", "last_login", "is_superuser", "is_staff",
                  "is_active", "date_joined"]
        read_only_fields = ["last_login", "is_active", "id", "date_joined"]

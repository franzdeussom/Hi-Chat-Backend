from rest_framework import serializers

from users.models import User


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "profile", "account_type", "is_active"]


class UserDetailSerializer(serializers.ModelSerializer):
    followers = serializers.SerializerMethodField()
    followings = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', "first_name", "last_name", "password", "email", "age",
                  "gender", "phone", "birthday", "country", "city", "profile",
                  "account_type", "last_login", "is_superuser", "is_staff",
                  "followers", "followings", "is_active", "date_joined"]
        read_only_fields = ["id", "password", "last_login", "is_active", "date_joined"]

    def to_representation(self, instance: User):
        data = super().to_representation(instance)
        if self.context["request"].user != instance:
            del data['password']
        return data

    def get_followers(self, instance: User):
        return instance.followers.count()

    def get_followings(self, instance: User):
        return instance.followings.count()

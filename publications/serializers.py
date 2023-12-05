from typing import Union

from rest_framework import serializers

from publications.models import Publication, Comment
from users.serializers import UserListSerializer


class UserCreationSerializer(serializers.ModelSerializer):
    already_like = serializers.SerializerMethodField()
    owner = serializers.SerializerMethodField()

    def get_already_like(self, instance: Union[Publication, Comment]):
        return self.context["request"].user in instance.likes.all()

    def get_owner(self, instance: Union[Publication, Comment]):
        return UserListSerializer(instance=instance.owner).data


class PublicationSerializer(UserCreationSerializer):
    nb_comments = serializers.SerializerMethodField()

    class Meta:
        model = Publication
        fields = ['id', 'owner', 'body', 'media', 'background', 'nb_likes', 'nb_comments', 'already_like', 'public',
                  'kind', 'pub_date']
        depth = 1

    def get_nb_comments(self, instance: Publication):
        return instance.comments.count()


class CommentSerializer(UserCreationSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'publication', 'owner', 'body', 'nb_likes', 'already_like', 'comment_date']

from rest_framework import serializers

from publications.models import Publications


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publications
        fields = ['id', 'user', 'body', 'media', 'background', 'likes', 'public', 'kind', 'pub_date']


class PublicationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publications
        fields = ['id', 'user', 'body', 'media', 'background', 'likes', 'public', 'kind', 'pub_date']


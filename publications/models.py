import uuid

from django.conf import settings
from django.db import models, transaction


def user_publication_upload_location(instance, filename):
    return f"{instance.user.id}/publications/{instance.id}/{uuid.uuid4()}{filename[filename.rfind('.'):]}"


class LikeManagerMixin:
    likes = None

    def nb_likes(self):
        return self.likes.count()


class Publication(models.Model, LikeManagerMixin):
    class Kind(models.TextChoices):
        VIDEO = "VIDEO"
        IMAGE = "IMAGE"
        __empty__ = "(Not Defined)"

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='publications')
    body = models.TextField('description', null=True)
    media = models.FileField(upload_to=user_publication_upload_location, null=True)
    background = models.CharField(max_length=1024, null=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_publications')
    public = models.BooleanField(default=True)
    kind = models.CharField("type publication", max_length=10, choices=Kind.choices, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body


class Comment(models.Model, LikeManagerMixin):
    publication = models.ForeignKey(Publication, related_name='comments', on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='publications_comments')
    body = models.TextField('description')
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_publications_comments')
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

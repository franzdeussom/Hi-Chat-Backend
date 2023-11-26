import time

from django.contrib.auth import get_user_model
from django.db import models


def user_publication_upload_location(instance, filename):
    return f"{instance.user.id}/publications/{instance.id}/{time.time()}{filename[filename.rfind('.'):]}"


class Publications(models.Model):
    class Kind(models.TextChoices):
        VIDEO = "VIDEO"
        IMAGE = "IMAGE"
        __empty__ = "(Not Defined)"

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='publications')
    body = models.TextField('description', null=True)
    media = models.FileField(upload_to=user_publication_upload_location, null=True)
    background = models.CharField(max_length=1024, null=True)
    likes = models.ManyToManyField(get_user_model(), related_name='liked_publications')
    public = models.BooleanField(default=False)
    kind = models.CharField("type publication", max_length=10, choices=Kind.choices, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    publication = models.ForeignKey(Publications, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField('description')
    likes = models.ManyToManyField(get_user_model(), related_name='liked_publ_comments')
    comment_date = models.DateTimeField(auto_now_add=True)


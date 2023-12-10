from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User


class Message(models.Model):
    class Status(models.TextChoices):
        SENT = 'SENT', _('sent')
        RECEIVED = 'RECEIVED', _('received')
        __empty__ = _('(unknown)')

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    body = models.TextField('contenu')
    sent_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=Status.choices)

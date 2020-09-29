from django.contrib.auth.models import User
from django.db import models


class DirectMessage(models.Model):
    sender = models.ForeignKey(User, related_name="sender", related_query_name="sender", on_delete=models.SET_NULL, null=True)
    receiver = models.ForeignKey(User, related_name="receiver", related_query_name="receiver", on_delete=models.SET_NULL, null=True)
    message_content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    isOpened = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at']
        verbose_name = 'DirectMessage'
        verbose_name_plural = 'DirectMessages'

    def __str__(self):
        return 'Message from: ' + self.sender.username + ' -> ' + self.receiver.username

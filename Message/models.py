from django.contrib.auth.models import User
from django.db import models
from django.db.models import Max


class DirectMessage(models.Model):
    user = models.ForeignKey(User, related_name='m_user', on_delete=models.CASCADE, null=True)
    sender = models.ForeignKey(User, related_name="from_user", related_query_name="sender", on_delete=models.SET_NULL,
                               null=True)
    receiver = models.ForeignKey(User, related_name="to_user", related_query_name="receiver", on_delete=models.SET_NULL,
                                 null=True)
    message_content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    isOpened = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at']
        verbose_name = 'DirectMessage'
        verbose_name_plural = 'DirectMessages'

    def __str__(self):
        return 'Message from: ' + self.sender.username + ' -> ' + self.receiver.username

    def send_message(from_user, to_user, message_content):
        sender_message = DirectMessage(
            user=from_user,
            sender=from_user,
            receiver=to_user,
            message_content=message_content,
            isOpened=True
        )
        sender_message.save()

        recipient_message = DirectMessage(
            user=to_user,
            sender=from_user,
            message_content=message_content,
            receiver=to_user)
        recipient_message.save()

        return sender_message

    def get_message(user):
        users = []
        messages = DirectMessage.objects.filter(user=user).values('receiver').annotate(last=Max('created_at')).order_by(
            '-last')
        for message in messages:
            users.append({
                'user': User.objects.get(pk=message['receiver']),
                'last': message['last'],
            })
        return users

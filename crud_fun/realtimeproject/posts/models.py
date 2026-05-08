# posts/models.py

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class Post(models.Model):

    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


@receiver(post_save, sender=Post)
def post_created(sender, instance, created, **kwargs):

    if created:

        channel_layer = get_channel_layer()

        async_to_sync(channel_layer.group_send)(
            'posts',
            {
                'type': 'send_post',
                'title': instance.title
            }
        )
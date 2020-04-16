from django.db.models.signals import post_save
from django.dispatch import receiver
import requests
from posts.models import Comment
from .models import Notification

from django.shortcuts import get_object_or_404
from posts.models import Comment, Post

def create_comment_notifications(comment_id):
    try:
        comment = Comment.objects.get(id=comment_id)
    except model.DoesNotExist:
        comment = None

    if not comment:
        return

    notification = Notification.objects.create(
        content = f'{comment.author} commented on your post.',
        post = comment.post,
        receiver = comment.post.author,
        sender = comment.author,
    )
    requests.get('http://localhost:3000/new/{}'.format(user_id))
    print(user_id)


@receiver(post_save, sender=Comment, dispatch_uid='notification_coment_post_save')
def notification_comment_post_save(sender, instance=None, created=None, **kwargs):
    if not created:
        return

    create_comment_notifications(instance.id)

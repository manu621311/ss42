from django.db.models.signals import post_save
from django.dispatch import receiver
import requests
from .models import Post, Img, Message
from objects.models import Profile

def inc_scoin_post(post_id):
    try:
        post = Post.objects.get(id=post_id)
    except:
        post = None
    
    if not post:
        return

    try:
        obj = Profile.objects.get(username=post.author.username)
        val = obj.Scrapcoins
        obj.Scrapcoins = val + 1
        obj.save()
    except:
        obj = Profile.objects.create(
            username=post.author.username,
            tags = [""],
            Scrapcoins = 1
            )

def inc_scoin_img(post_id):
    try:
        img = Img.objects.get(id=post_id)
    except:
        img = None
    
    if not img:
        return

    try:
        obj = Profile.objects.get(username=img.author.username)
        val = obj.Scrapcoins
        obj.Scrapcoins = val + 3
        obj.save()
    except:
        obj = Profile.objects.create(
            username=img.author.username,
            tags = [""],
            Scrapcoins = 1
            )


@receiver(post_save, sender=Post, dispatch_uid='post_scoin_inc')
def post_scoin_inc(sender, instance=None, created=None, **kwargs):
    if not created:
        return

    inc_scoin_post(instance.id)

@receiver(post_save, sender=Img, dispatch_uid='img_scoin_inc')
def img_scoin_inc(sender, instance=None, created=None, **kwargs):
    if not created:
        return

    inc_scoin_img(instance.id)
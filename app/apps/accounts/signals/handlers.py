from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models import Profile

User = get_user_model()


@receiver(signal=post_save, sender=User)
def create_author(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

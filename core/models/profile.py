from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    notes = models.TextField(blank=True, null=True, default="")
    skype = models.TextField(blank=True, null=True, default="")
    phone = models.CharField(blank=True, null=True, default="", max_length=128)
    status = models.TextField(blank=True, null=True, default="")
    image = models.TextField(blank=True, null=True, default="")

    class Meta:
        db_table = "core_profiles"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

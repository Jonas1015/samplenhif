from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from rest_framework.authtoken.models import Token



@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)


@receiver(post_save, sender = User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()



@receiver(post_save, sender = User)
def create_auth_token(sender, instance = None, created = False, **kwargs):
    if created:
        Token.objects.create(user = instance)

# @receiver(post_save, sender=User, dispatch_uid = 'save_new_user_profile')
# def save_profile(sender, instance, created, **kwargs):
#     user = instance
#     if created:
#         profile = Profile(user=user)
#         profile.save()

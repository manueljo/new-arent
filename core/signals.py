from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail, BadHeaderError
from .models import Profile,User


@receiver(post_save, sender=User)
def send_booking_mail(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
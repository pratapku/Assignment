from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    notes_data=models.TextField()
    thumbnail=models.ImageField(upload_to='images/')
    created_at=models.DateTimeField(auto_now_add=True)
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
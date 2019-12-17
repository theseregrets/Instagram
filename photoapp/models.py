from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	bio=models.TextField(max_length=500, blank=True)
	birthdate=models.DateField(null=True,blank=True)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

@receiver(post_save,sender=User)

def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Post(models.Model):
	title=models.CharField(max_length=100)
	content=models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author=models.ForeignKey(User,on_delete=models.CASCADE)
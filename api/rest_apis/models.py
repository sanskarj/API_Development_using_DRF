from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractBaseUser,User



# Create your models here.

class userinfo(models.Model):
    name = models.CharField(max_length=32)
    location = models.CharField(max_length=200)
    aboutme = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
class profileimage(models.Model):
    profile_image_url = models.URLField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class communication(models.Model):
    medium = models.CharField(max_length=100)
    medium_url = models.URLField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class hobby(models.Model):
    name = models.CharField(max_length=32)
    hobby_image_url =  models.URLField()
    users = models.ManyToManyField(User)
class skills(models.Model):
    name = models.CharField(max_length=32)
    proficiency = models.IntegerField()
    users = models.ManyToManyField(User)

class projects(models.Model):
    info = models.CharField(max_length=32)
    starts = models.DateField()
    ends = models.DateField()
    status = models.CharField(max_length=32)
    description = models.CharField(max_length=300)
    users = models.ManyToManyField(User)
class achievements(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=32)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class chat(models.Model):
    receiver = models.ForeignKey(User,on_delete=models.CASCADE,related_name="receiver")
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name="sender")
    message = models.CharField(max_length=200)
    

    
    
    



@receiver(post_save,sender=User)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)









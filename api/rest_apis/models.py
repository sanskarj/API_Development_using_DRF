from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractBaseUser,User



# Create your models here.

class Industries(models.Model):
    name = models.TextField()
class languages(models.Model):
    name = models.TextField()
class userinfo(models.Model):
    name = models.CharField(max_length=32)
    location = models.CharField(max_length=200)
    aboutme = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)


class communication(models.Model):
    medium = models.CharField(max_length=100)
    medium_url = models.URLField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class hobby(models.Model):
    name = models.CharField(max_length=32)
    users = models.ManyToManyField(User)
class skills(models.Model):
    name = models.CharField(max_length=32)
    competancy = models.CharField(max_length=32)
    users = models.ManyToManyField(User)
class Skill_names(models.Model):
    name = models.CharField(max_length=32)

class projects(models.Model):
    info = models.CharField(max_length=32)
    starts = models.DateField()
    ends = models.DateField()
    status = models.CharField(max_length=32)
    #new fields
    project_description = models.CharField(max_length=300)
    project_details = models.TextField()   #business problem
    proposed_solution = models.TextField()  #solution description
    multi_vendor = models.BooleanField()  #multiple vendors
    benefits = models.TextField()
    #ends here   
    users = models.ManyToManyField(User)
    skills = models.ManyToManyField(Skill_names)
    client_name = models.TextField()
    client_location = models.TextField()
    location_of_project_execution = models.TextField()
    Industry_of_the_client = models.TextField()
    Role = models.TextField()
    team_size = models.TextField()
    #case_study_submitted = models.TextField()
class achievements(models.Model):
    date = models.TextField()
    title = models.CharField(max_length=32)
    description  = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class chat(models.Model):
    receiver = models.ForeignKey(User,on_delete=models.CASCADE,related_name="receiver")
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name="sender")
    message = models.CharField(max_length=200)
class badge(models.Model):
    title = models.CharField(max_length=32)
    image_url = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class certification(models.Model):
    title = models.TextField()
    organization  = models.TextField()
    certificate_type = models.TextField()
    year = models.CharField(max_length=4)
    certificate = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
class education(models.Model):
    degree = models.TextField()
    institute = models.TextField()
    year = models.CharField(max_length=4)
    specialization = models.TextField()
    gpa = models.TextField()
    status = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
class blog(models.Model):
    title = models.TextField()
    description = models.TextField()
    link = models.URLField()
    blog_site = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    
    
    



@receiver(post_save,sender=User)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)









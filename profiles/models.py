from django.db import models
from django.contrib.auth.models import User

class Gender(models.Model):
  gender = models.CharField(max_length = 20)
  
  def __unicode__(self):
    return "%s" % self.gender

class UserProfile(models.Model):
  user = models.ForeignKey(User, unique=True)
  
  avatar = models.ImageField(upload_to = 'profiles', blank=True)  
  location = models.CharField(max_length = 100, blank=True)
  website = models.URLField(blank=True)
  intro = models.TextField(blank=True)
  employment = models.CharField(max_length = 100, blank=True)
  education = models.CharField(max_length = 100, blank=True)
  gender = models.ForeignKey(Gender, null = True)
  other_names = models.CharField(max_length = 250, blank=True)
  birthday = models.DateField('Birthdate', blank=True)
  
  def __unicode__(self):
    return "%s" % self.user
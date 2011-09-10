from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
  
  author = models.ForeignKey(User, related_name = "article_author")
  title = models.CharField(max_length = 120)
  content = models.TextField()
  published = models.BooleanField(default = False)
  pub_date = models.DateTimeField('date published')

  def __unicode__(self):
    return self.title
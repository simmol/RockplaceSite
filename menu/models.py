from django.db import models

class Menu(models.Model):
  name = models.CharField(max_length = 100)
  slug = models.SlugField()
  base_url = models.CharField(max_length = 100, blank = True, null = True)
  description = models.TextField(blank = True, null = True)
  
  def __unicode__(self):
    return "%s" % self.name
  
  def save(self):
    super(Menu, self).save()
    
    current = 10
    for item in MenuItem.objects.filter(menu = self).order_by('order'):
      item.order = current
      item.save()
      current += 10
      
      
class MenuItem(models.Model):
  menu = models.ForeignKey(Menu)
  order = models.IntegerField()
  link_url = models.URLField(max_length = 100)
  title = models.CharField(max_length = 100)
  login_required = models.NullBooleanField()
  
  def __unicode__(self):
    return "%s %s.%s" % (self.menu.slug, self.order, self.title)

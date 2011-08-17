from news.models import Article
from django.contrib import admin

class ArticleAdmin(admin.ModelAdmin):
  pass

admin.site.register(Article, ArticleAdmin)
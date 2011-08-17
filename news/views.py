# Django
from django.shortcuts import render_to_response
from django.template import Context, loader
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from news.models import Article

def index(request):
  latest_article_list = Article.objects.all().order_by('-pub_date')[:]
  return render_to_response('news/index.html', {'latest_article_list':latest_article_list})

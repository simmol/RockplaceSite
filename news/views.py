# Django
from django.shortcuts import render_to_response
from django.template import Context, loader
from django.http import HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from news.models import Article
from rockplacesite import settings


def index(request):
  article_list = Article.objects.filter(published = 1).order_by('-pub_date')[:]
  paginator = Paginator(article_list, settings.NEWS_PER_PAGE)
  
  page = request.GET.get('page', 1)
  try:
    latest_article_list = paginator.page(page)
  except PageNotAnInteger:
    latest_article_list = paginator.page(1)
  except EmptyPage:
    latest_article_list = paginator.page(paginator.num_pages)
    
  return render_to_response('news/index.html', {'latest_article_list':latest_article_list})

def details(request, news_id):
  try:
    article = Article.objects.get(pk=news_id, published=1)
  except Article.DoesNotExist:
    raise Http404
  return render_to_response('news/details.html', {'article':article})
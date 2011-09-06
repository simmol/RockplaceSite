from django.conf.urls.defaults import *

urlpatterns = patterns('news.views',
    (r'^article/(?P<news_id>\d+)$', 'details'),
    (r'^$', 'index' ),
)
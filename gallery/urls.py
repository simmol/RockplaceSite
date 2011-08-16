from django.conf.urls.defaults import *

urlpatterns = patterns('gallery.views',
    (r'^$', 'index' ),
    url(r'^album/(\d+)/$', 'album', name="name-album"),
)

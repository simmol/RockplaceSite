from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Admin:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

    #(r'^gallery/', include("gallery.urls")),
    (r'^news/', include("news.urls")),
    (r'^$', 'django.views.generic.simple.direct_to_template',
              {'template': 'home.html'}),
    
    (r'^comments/', include('django.contrib.comments.urls')),

)

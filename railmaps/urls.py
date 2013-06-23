from django.conf.urls import patterns, include, url
from main.views import hello
import tdcenter.urls
# Django Admin 
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^test/$', hello, name='hello'),
	url(r'^center/', include('tdcenter.urls')),
    # Examples:
    # url(r'^$', 'railmaps.views.home', name='home'),
    # url(r'^railmaps/', include('railmaps.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

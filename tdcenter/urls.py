# _*_ coding: utf-8 _*_
from django.conf.urls import patterns, include, url
from tdcenter.views import *
'''
	工程中心主页url
'''
urlpatterns = patterns('',
	url(r'^main/$', main),
	url(r'^stuff/$', stuff),
	url(r'^research/$', research),
	url(r'^equipment/$', equipment),
    # Examples:
    # url(r'^$', 'railmaps.views.home', name='home'),
    # url(r'^railmaps/', include('railmaps.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
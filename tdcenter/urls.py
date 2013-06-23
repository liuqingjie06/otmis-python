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
)
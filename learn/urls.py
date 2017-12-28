#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Lids'
__mtime__ = '2017/12/7'
"""
from django.conf.urls import url
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from learn import views
from learn.views import FileUploadView

urlpatterns = [
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^files/$', views.FileList.as_view()),
    url(r'^files/(?P<pk>[0-9]+)/$', views.FileDetail.as_view()),
    url(r'^upload/(?P<filename>[^/]+)$', FileUploadView.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

urlpatterns = format_suffix_patterns(urlpatterns)
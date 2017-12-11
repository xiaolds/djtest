#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Lids'
__mtime__ = '2017/12/7'
"""
from django.conf.urls import url
from django.contrib.auth.models import User
from django.urls import path, include
from rest_framework import viewsets, serializers, routers

from learn import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /learn/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /learn/5/results
    path('<int:question_id>/results', views.results, name='results'),
    # ex: /learn/5/vote/
    path('<int:question_id>/vote', views.vote, name='vote'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
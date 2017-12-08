#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Lids'
__mtime__ = '2017/12/7'
"""
from django.urls import path

from learn import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /learn/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /learn/5/results
    path('<int:question_id>/results', views.results, name='results'),
    # ex: /learn/5/vote/
    path('<int:question_id>/vote', views.vote, name='vote'),
    path('users/', views.users, name='all_user'),
    path('users/<int:user_id>', views.single_user, name='user_detail')

]
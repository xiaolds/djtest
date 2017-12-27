#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Lids'
__mtime__ = '2017/12/18'
"""
from rest_framework import serializers
from learn.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_name', 'user_sex', 'user_email',
                  'user_phone', 'user_register_time', 'user_login_time')
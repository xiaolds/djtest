#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Lids'
__mtime__ = '2017/12/18'
"""
from django.contrib.auth.models import User
from rest_framework import serializers
from learn.models import File


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ('user_name', 'user_sex', 'user_email',
        #           'user_phone', 'user_register_time', 'user_login_time')
        fields = ('id', 'username', 'files')


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('file_name', 'file_create_time', 'file_update_time', 'owner')

    owner = serializers.ReadOnlyField(source='owner.username')
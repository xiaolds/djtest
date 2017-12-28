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
    files = serializers.StringRelatedField(many=True)
    # files = serializers.PrimaryKeyRelatedField(many=True, required=False, read_only=True)
    file_count = serializers.SerializerMethodField()
    # files = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'files', 'file_count')

    def get_file_count(self, obj):
        return obj.files.all().count()


class FileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = File
        fields = ('id', 'file_name', 'file_create_time', 'file_update_time', 'owner')
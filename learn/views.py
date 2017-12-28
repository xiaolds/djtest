import time
from io import BytesIO

import pytz
from django.contrib.auth.models import User

from rest_framework import generics, permissions, views
from rest_framework.parsers import FileUploadParser, JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from learn.models import File
from learn.permissions import IsOwnerOrReadOnly
from learn.serializers import UserSerializer, FileSerializer
from datetime import datetime


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = (permissions.IsAuthenticated,)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = (permissions.IsAuthenticated,
                          IsOwnerOrReadOnly,)


class FileList(generics.ListCreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


# views.py
class FileUploadView(views.APIView):
    parser_classes = (FileUploadParser,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def put(self, request, filename, format=None):
        # up_file = request.FILES.get("file", None)
        up_file = request.data['file']
        try:
            destination = open('D:/test/' + up_file.name, 'wb+')
            for chunk in up_file.chunks():
                print(chunk)
                destination.write(chunk)
            destination.close()
            # 保存成功后入库
            t = datetime.now(tz=pytz.UTC)
            file = File(owner=request.user, file_name=up_file.name, file_create_time=t, file_update_time=t)
            # old_file = File.objects.get(file_name=up_file.name)
            file_count = File.objects.filter(file_name=up_file.name).count()
            if file_count == 0:
                file.save()
            else:
                old_file = File.objects.get(file_name=up_file.name)
                old_file.file_update_time = file.file_update_time
                old_file.owner = file.owner
                old_file.file_name = file.file_name
                old_file.save()
            file_ser = FileSerializer(file)
            return Response(status=201, data=JSONRenderer().render(file_ser.data))
        except Exception as e:
            print(e)
            return Response(status=500, data=str(e))





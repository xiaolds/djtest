from rest_framework.decorators import api_view
from rest_framework.response import Response

from learn.models import User
from learn.serializers import UserSerializer


@api_view(['GET'])
def user_list(request, format=None):
    if request.method == 'GET':
        users = User.objects.all()
        s_users = UserSerializer(users, many=True)
        return Response(s_users.data)
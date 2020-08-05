from django.shortcuts import render
from rest_framework.generics import GenericAPIView
# Create your views here.
from rest_framework.response import Response

from home.models import AxfUser
from user.userserializers import UserSerializer

class UserShowView(GenericAPIView):
    queryset = AxfUser.objects.all()
    serializer_class = UserSerializer

    def get(self, request):
        # 获取token值
        token = request.query_params.get('token')
        print(token)
        # 从token
        return Response({
            'code': 1
        })
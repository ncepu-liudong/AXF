from django.shortcuts import render

# Create your views here.
from rest_framework.exceptions import APIException
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from cart.cartserializers import CartAddSerializer
from home.models import AxfUser, AxfCart
from user.util import token_confirm


class CartAddView(CreateAPIView):
    queryset = AxfUser
    serializer_class = CartAddSerializer

    def create(self, request, *args, **kwargs):
        # 生成序列化器
        serializer = self.get_serializer(data=request.data)
        # 认证......

        # 获取token
        token = request.query_params.get('token')
        try:
            uid = token_confirm.confirm_validate_token(token)
        except APIException as e:
            print(e)
            return Response({
                'code': 1006,
                'msg': 'token失效',
                'data': {}
            })
        try:
            user = AxfUser.objects.get(pk=uid)
        except APIException as e:
            print(e)
            return Response({
                'code': 1006,
                'msg': '用户不存在',
                'data': {}
            })

        if serializer.is_valid():
            # 商品存在
            # 找到购物车中用户的商品记录
            carts = AxfCart.objects.filter()
        else:
            return Response({
                'code': 1006,
                'msg': '商品不存在',
                'data': {}
            })

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
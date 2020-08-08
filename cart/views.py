from django.shortcuts import render

# Create your views here.
from rest_framework.exceptions import APIException
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response

from cart.CartPermissions import CartPermission
from cart.MyAuthentications import CartAuthentication
from cart.cartserializers import CartAddSerializer, CartSerializer
from home.models import AxfUser, AxfCart, AxfGoods
from user.util import token_confirm


class CartAddView(CreateAPIView):
    '''
    商品加入到购物车
    '''
    queryset = AxfUser
    serializer_class = CartAddSerializer
    authentication_classes = CartAuthentication,
    permission_classes = CartPermission,

    def create(self, request, *args, **kwargs):
        # 生成序列化器
        serializer = self.get_serializer(data=request.data)
        user = request.user
        if isinstance(user, AxfUser):
            return Response({
                'code': 105,
                'msg': '用户未登录',
                'data':{ }
            })
        if serializer.is_valid():
            # 商品存在
            # 找到购物车中用户的商品记录
            carts = AxfCart.objects.filter(c_user=user)
            goodsid = serializer.data.get('goodsid')
            the_good = AxfGoods.objects.get(pk=goodsid)
            carts = carts.filter(c_goods = the_good)
            # 购物车中存在该种商品的记录
            if carts.exists():
                cart = carts.first()  # 得到购物车中该商品记录
                cart.c_goods_num += 1  # 商品数量加1
                cart.save()
            else: # 购物车中没有该商品
                cart = AxfCart()
                cart.c_goods_num = 1
                cart.c_goods = the_good
                cart.c_user = user
                cart.c_is_select = 1
                cart.save()
            return Response({
                'code': 200,
                'msg': 'ok',
                'data': {
                    'c_goods_num': cart.c_goods_num
                }
            })
        else:
            return Response({
                'code': 1006,
                'msg': '商品不存在',
                'data': {}
            })

class CartListView(ListAPIView):
    queryset = AxfCart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = CartAuthentication,
    permission_classes = CartPermission,

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        user = request.user
        # 看到自己的购物车记录
        queryset = queryset.filter(c_user=user)
        queryset = self.filter_queryset(queryset)
        # 计算总价
        total = 0
        for rec in queryset:
            total += rec.c_goods_num * rec.c_goods.price
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'code': 200,
            'msg': '查询成功',
            'data': {
                'title': '购物车',
                'is_all_select': True,
                'total_price': total,
                'carts': serializer.data
            }
        })

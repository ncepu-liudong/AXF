from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from home.homeserializers import WheelSerializer, NavSerializer, ShopSerializer, MainshowSerializer, MustbuySerializer
from home.models import AxfWheel, AxfNav, AxfShop, AxfMainshow, AxfMustbuy


class HomeListView(GenericAPIView):
    '''
    get:
    获取首页数据
    '''
    queryset = AxfWheel.objects.all()
    serializer_class = WheelSerializer
    def get(self, request):
        # 数据查询
        nav_queryset = AxfNav.objects.all()
        shop_queryset = AxfShop.objects.all()
        mainshow_queryset = AxfMainshow.objects.all()
        mustbuy_queryset = AxfMustbuy.objects.all()

        # 序列化
        nav_data = NavSerializer(nav_queryset, many=True)
        shop_data = ShopSerializer(shop_queryset, many=True)
        mainshow_data = MainshowSerializer(mainshow_queryset, many=True)
        mustbuy_data = MustbuySerializer(mustbuy_queryset, many=True)
        wheel_data = self.serializer_class(self.queryset.all(), many=True)

        return Response({
            'code': 200,
            'msg': '请求成功',
            'data': {
                'main_wheels': wheel_data.data,
                'main_navs': nav_data.data,
                'main_shops': shop_data.data,
                'main_shows': mainshow_data.data,
                'main_mustbuys': mustbuy_data.data
            }
        })


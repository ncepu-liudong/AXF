from rest_framework import serializers

from home.models import AxfGoods, AxfCart
from market.marketserializers import GoodsSerializer


class CartAddSerializer(serializers.Serializer):
    goodsid = serializers.CharField(required=True)
    token = serializers.CharField()
    def validate_goodsid(self, value):
        value = int(value)
        goods = AxfGoods.objects.filter(pk=value).first()
        if not goods:
            raise serializers.ValidationError("商品不存在")
        return value

    def validate_token(self, data):
        if not data:
            raise serializers.ValidationError("token不存在")
        return data

class CartSerializer(serializers.ModelSerializer):
    # 关联序列化
    c_goods = GoodsSerializer()
    class Meta:
        model = AxfCart
        fields = "__all__"
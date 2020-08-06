from rest_framework import serializers

from home.models import AxfGoods


class CartAddSerializer(serializers.Serializer):
    goodsid = serializers.CharField(required=True)

    def Validate_goodsid(self, value):
        value = int(value)
        goods = AxfGoods.objects.filter(pk=value).first()
        if not goods:
            raise serializers.ValidationError("商品不存在")
        return value
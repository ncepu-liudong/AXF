from home.models import AxfUser
from rest_framework import serializers

# 用户序列化器
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AxfUser
        fields = '__all__'
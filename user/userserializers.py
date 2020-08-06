from django.contrib.auth.hashers import make_password, check_password

from home.models import AxfUser
from rest_framework import serializers

# 用户序列化器
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AxfUser
        fields = '__all__'

class UserRegisterSerializer(serializers.Serializer):
    u_username = serializers.CharField(required=True)
    u_password = serializers.CharField(min_length=1, max_length=20,
                                       error_messages={
                                           'max_length': '最大长度不超过20字符',
                                           'min_length': '最小长度不少于1字符'
                                       })
    u_password2 = serializers.CharField(min_length=1, max_length=20,
                                       error_messages={
                                           'max_length': '最大长度不超过20字符',
                                           'min_length': '最小长度不少于1字符'
                                       })
    u_email = serializers.EmailField(required=True)

    # 验证用户名是否唯一
    def validate_u_username(self, attrs):
        user = AxfUser.objects.filter(u_username=attrs).first()
        if user:
            raise serializers.ValidationError("用户名已经存在")
        return attrs

    # 全局验证
    def validate(self, attrs):
        password = attrs.get('u_password')
        password2 = attrs.get('u_password2')
        if password != password2:
            raise serializers.ValidationError({'u_password': "两次密码不一致"})
        return attrs

    # 涉及到两个password不能直接进行序列化保存
    def create(self, validated_data):
        user = AxfUser()
        password = validated_data.get('u_password')
        password = make_password(password)   # 密码加密操作
        user.u_username = validated_data.get('u_username')
        user.u_password = password
        user.u_email = validated_data.get('u_email')
        user.is_active = 1
        user.is_delete = 0
        user.save()
        return user

# 登录序列化器
class LoginSerializer(serializers.Serializer):
    u_username = serializers.CharField(min_length=1, required=True)
    u_password = serializers.CharField(required=True,min_length=1)

    def validate(self, attrs):
        username = attrs.get('u_username')
        password = attrs.get('u_password')
        user = AxfUser.objects.filter(u_username=username)
        # 判断是否有该用户
        if not user.exists():
            raise serializers.ValidationError({'username': '用户不存在'})
        # 验证通过，用户存在
        user = user.first()
        # check_password(明文密码，加盐密码)，如果相等返回true
        if not check_password(password, user.u_password):
            raise serializers.ValidationError({'invalid': '用户名或者密码错误'})
        return attrs
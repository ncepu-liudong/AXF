from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from home.models import AxfUser
from user.util import token_confirm


class CartAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # 获取token
        token = request.data.get('token', None) or request.query_params.get('token', None)
        try:
            uid = token_confirm.confirm_validate_token(token)
        except Exception as e:
            #
            return
        try:
            user = AxfUser.objects.get(pk=uid)
        except Exception as e:
            #
            return
        # 验证成功
        return user,token
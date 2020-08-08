from rest_framework.permissions import BasePermission

from home.models import AxfUser


class CartPermission(BasePermission):
    def has_permission(self, request, view):
        # 只有登录用户返回True,未登录返回false
        return isinstance(request.user, AxfUser)

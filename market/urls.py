from django.contrib import admin
from django.urls import path, include

from market import views

app_name = 'market'
urlpatterns = [
    # 商品类型列表
    path('goodtype/', views.GoodTpyeListView.as_view(), name='goodtype'),
    # 商品信息列表
    path('market/', views.GoodsListView.as_view(), name='market'),
]
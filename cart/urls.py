from django.contrib import admin
from django.urls import path, include

from cart import views

app_name = 'cart'
urlpatterns = [
    path('cart/add_cart/', views.CartAddView.as_view(), name='add'),
    path('cart/', views.CartListView.as_view(), name='list'),
]
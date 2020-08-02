from django.contrib import admin
from django.urls import path, include

from market import views

app_name = 'market'
urlpatterns = [
    path('index/', views.GoodTpyeListView.as_view(), name='goodtype'),
]
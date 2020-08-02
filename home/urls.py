from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

from home import views

app_name = 'home'
urlpatterns = [
    path('index/', views.HomeListView.as_view(), name='home'),
]
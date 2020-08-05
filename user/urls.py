from django.urls import path
from user import views

app_name = 'user'
urlpatterns = [
    path('auth/', views.UserShowView.as_view(), name='user'),
]
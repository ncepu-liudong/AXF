from django.urls import path
from user import views

app_name = 'user'
urlpatterns = [
    path('auth/', views.UserShowView.as_view(), name='user'),
    path('auth/register/', views.UserRegisterView.as_view(), name='register'),
    path('auth/login/', views.UserLoginView.as_view(), name='login'),
]
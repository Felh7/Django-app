from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'users'

urlpatterns = [
    path("", views.home.as_view(), name='home'),
    path("login", views.LoginUser.as_view(), name='login'),
    path("register", views.RegisterUser.as_view(), name='register'),
    path("logout", LogoutView.as_view(), name='logout' ),
]
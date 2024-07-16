from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


app_name = 'users'

urlpatterns = [
    path("", views.home, name='home'),
    path("login", views.LoginUser.as_view(), name='login'),
    path("register", views.register_page, name='register'),
    path("logout", LogoutView.as_view(), name='logout' )

]
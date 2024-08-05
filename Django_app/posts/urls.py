from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'posts'

urlpatterns = [
    path('addpost', views.post_page.as_view(), name='posts'),
    path('subscribe_ajax', views.subscribe_ajax, name = 'subscribe_ajax'),
    path('<str:username>', views.profile_page.as_view(),name='profile'),
]
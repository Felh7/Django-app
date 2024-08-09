from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'posts'

urlpatterns = [
    path('addpost', views.post_page.as_view(), name='add_post'),
    path('subscribe_ajax', views.subscribe_ajax, name = 'subscribe_ajax'),
    path('unsubscribe_ajax', views.unsubscribe_ajax, name = 'unsubscribe_ajax'),
    path('checksubscription_ajax',views.checksubscription_ajax, name = 'checksubscription_ajax'),
    path('likePost_ajax', views.likePost_ajax, name = 'likepost_ajax'),
    path('unlikePost_ajax', views.unlikePost_ajax, name = 'unlikepost_ajax'),
    path('CheckIfLiked_ajax',views.CheckIfLiked_ajax, name = 'checkifliked_ajax'),
    path('<str:username>', views.profile_page.as_view(),name='profile'),
]
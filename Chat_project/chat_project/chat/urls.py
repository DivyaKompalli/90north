from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_view, name='chat'),
    path('signup/', views.signup_view, name='signup'),
    path('index/', views.login_view, name='index'),
    path('logout/', views.logout_view, name='logout'),
    path('chat/<int:user_id>/', views.chat_view, name='chat_with_user'),
]
from django.urls import re_path
from .views import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatConsumer.as_asgi()),
]

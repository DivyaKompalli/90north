from django.contrib import admin
from django.urls import path, include
from django.core.asgi import get_asgi_application

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),  
]

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat.urls import websocket_urlpatterns

application = ProtocolTypeRouter({
    "https": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})

"""
ASGI config for chat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""
print("--- Attempting to load chat.asgi ---")
import os
from . import routing
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack


print("Loading custom asgi.py")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    # Handle HTTP requests with Django's standard ASGI application
    "http": django_asgi_app,

    # Handle WebSocket connections
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns # Reference the urlpatterns from your app's routing.py
        )
    ),
})


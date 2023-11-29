import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chatapp.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mychatbot.settings')

# Initialize Django ASGI application to serve HTTP requests
django_asgi_app = get_asgi_application()

# Define the application protocol type router
application = ProtocolTypeRouter({
  # Django's ASGI application to handle traditional HTTP requests
  "http": django_asgi_app,

  # WebSocket chat handler
  "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})

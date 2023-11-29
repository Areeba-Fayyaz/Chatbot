# mychatbot/mychatbot/routing.py

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from chatapp.consumers import ChatConsumer  # Import your consumer from the app

websocket_urlpatterns = [
    path('ws/chat/', ChatConsumer.as_asgi()),  # Define the path for your WebSocket consumer
]

application = ProtocolTypeRouter({
    'websocket': URLRouter(websocket_urlpatterns),
    # You can also include HTTP routes here if needed
})
# mychatbot/mychatbot/routing.py (modified to include app-level routing)


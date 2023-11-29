# consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .tasks import save_chat_message
from .models import ChatMessage  
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Called when the websocket is handshaking as part of the connection process.
        await self.accept()

    async def disconnect(self, close_code):
        # Called when the websocket closes for any reason.
        pass

    async def receive(self, text_data):
        # Called with a text data payload when it's received.
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user = self.scope["user"]


        response = "This is a hardcoded response."
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
        'message': message,
        'sender': 'user'
        }))
        # Send hardcoded response
        await self.send(text_data=json.dumps({
            'message': response,
            'sender': 'chatbot'
        }))
        
        # Save the message to the database
        if user.is_authenticated:
            # Save user's message
            save_chat_message.delay(user.id, message)
            save_chat_message.delay(user.id, response, is_bot=True)


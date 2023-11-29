import json
import requests
from channels.generic.websocket import AsyncWebsocketConsumer
from .tasks import save_chat_message
from .models import ChatMessage  

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Called during the websocket handshake process.
        await self.accept()

    async def disconnect(self, close_code):
        # Called when the websocket closes for any reason.
        pass

    async def receive(self, text_data):
        # Called with a text data payload when received.
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user = self.scope["user"]

        # Sending message to Rasa server and receiving response
        rasa_response = requests.post(
            'http://localhost:5005/webhooks/rest/webhook',
            json={"sender": "user", "message": message}
        ).json()

        # Extract the response text
        response = rasa_response[0]['text'] if rasa_response else "Sorry, I didn't get that."

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': 'user'
        }))

        # Send response to WebSocket
        await self.send(text_data=json.dumps({
            'message': response,
            'sender': 'chatbot'
        }))

        # Save the message to the database if user is authenticated
        if user.is_authenticated:
            save_chat_message.delay(user.id, message)
            save_chat_message.delay(user.id, response, is_bot=True)

from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

class ChatMessage(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_bot = models.BooleanField(default=False)  # Indicates if the message is from the chatbot

    def __str__(self):
        return f"Message from {self.user.username}: {self.message[:30]}{'...' if len(self.message) > 30 else ''}"

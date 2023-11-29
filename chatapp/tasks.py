# chat/tasks.py
from mychatbot.celery import app

from celery import shared_task
from .models import ChatMessage

@shared_task
def save_chat_message(user_id, message, is_bot=False):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    user = User.objects.get(id=user_id)
    ChatMessage.objects.create(user=user, message=message, is_bot=is_bot)


from django.contrib import admin

# Register your models here.
#from home.models import Contact
#admin.site.register(Contact)
from .models import ChatMessage
admin.site.register(ChatMessage)
# @admin.register(ChatMessage)
# class ChatMessageAdmin(admin.ModelAdmin):
#     list_display = ('user', 'message', 'created_at', 'is_bot')
#     list_filter = ('created_at', 'user')
#     search_fields = ('message',)
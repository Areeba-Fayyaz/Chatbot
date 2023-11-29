from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('chat_home/', views.chat_home, name='chat_home'),
    # path('chat_with_bot/', views.chat_with_bot, name='chat_with_bot'),
    # Add other chat-related URLs here
]

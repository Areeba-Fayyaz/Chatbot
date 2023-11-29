from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .models import ChatMessage
import json
import requests
from django.http import JsonResponse,HttpResponseBadRequest

# Registration view
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'User has been registered successfully!')
            # login(request, user)
            return redirect('login')  # Redirect to chat home
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def chat_with_bot(request):
    user_message = request.GET.get("message")

    # Sending POST request to Rasa server
    response = requests.post(
        'http://localhost:5005/webhooks/rest/webhook',
        json={"sender": "user", "message": user_message}
    )

    # Get response from Rasa
    if response.status_code == 200:
        bot_message = response.json()[0]['text']
    else:
        bot_message = "I couldn't understand that. Please try again."

    return JsonResponse({"message": bot_message})


@login_required(login_url='/login/')
def chat_home(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Parse the JSON body of the request
        body = json.loads(request.body)

        if body.get('action') == 'clear_history':
            ChatMessage.objects.filter(user=request.user).delete()
            return JsonResponse({'status': 'success'})

        return HttpResponseBadRequest('Invalid request')
    message_history = ChatMessage.objects.filter(user=request.user).order_by('created_at')
    return render(request, 'chat_home.html', {'message_history': message_history})





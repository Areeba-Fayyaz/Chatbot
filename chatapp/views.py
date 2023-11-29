from django.shortcuts import render
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm

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

def chat_home(request):
    return render(request, 'chat_home.html')



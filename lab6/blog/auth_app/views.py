from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Проверка на пустые поля
        if not username or not email or not password:
            messages.error(request, "Все поля обязательны для заполнения")
            return render(request, 'register.html')
        
        # Проверка уникальности имени пользователя
        try:
            User.objects.get(username=username)
            messages.error(request, "Пользователь с таким именем уже существует")
            return render(request, 'register.html')
        except User.DoesNotExist:
            # Создание пользователя
            User.objects.create_user(username, email, password)
            messages.success(request, "Регистрация прошла успешно! Теперь вы можете войти.")
            return redirect('auth_app:login')
    
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Проверка на пустые поля
        if not username or not password:
            messages.error(request, "Все поля обязательны для заполнения")
            return render(request, 'login.html')
        
        # Аутентификация
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request, f"Добро пожаловать, {username}!")
            return redirect('archive')
        else:
            messages.error(request, "Неверное имя пользователя или пароль")
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    # messages.success(request, "Вы успешно вышли из системы")
    return redirect('archive')
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import ProfileForm, ChangePasswordForm
from .models import Profile
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from cars.models import Car
from likes.models import Like, Comment

def profile_detail_view(request, username):
    user_obj = get_object_or_404(User, username=username)
    profile = user_obj.profile
    comentarios = Comment.objects.filter(user=user_obj)
    likes = Like.objects.filter(user=user_obj)
    coleccion = None
    if profile.user_type == 'coleccionista':
        coleccion = Car.objects.filter(autor=user_obj)

    return render(request, 'accounts/profile_detail.html', {
        'profile_user': user_obj,
        'profile': profile,
        'comentarios': comentarios,
        'likes': likes,
        'coleccion': coleccion,
    })

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

class CustomLogoutView(LogoutView):
    next_page = '/'

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, user_type=request.POST.get('user_type', 'visitante'))  
            messages.success(request, 'Cuenta creada exitosamente. Inicia sesión.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado.')
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'accounts/profile.html', {'form': form})

@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Contraseña cambiada.')
            return redirect('profile')
    else:
        form = ChangePasswordForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})

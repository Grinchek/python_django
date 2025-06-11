from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import UserProfile
from django.contrib.auth import authenticate, login

def index_view(request):
    return render(request, 'mainapp/index.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            UserProfile.objects.create(user=user, image=request.FILES['image'])
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'mainapp/register.html', {'form': form})

def login_view(request):
    return render(request, 'mainapp/login.html')

def about_view(request):
    return render(request, 'mainapp/about.html')
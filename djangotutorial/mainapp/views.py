from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm, PostForm
from .models import UserProfile, Post
from django.http import HttpResponseForbidden, Http404

def index_view(request):
    return render(request, 'mainapp/index.html')

def about_view(request):
    return render(request, 'mainapp/about.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            image = form.cleaned_data.get('image')
            if image:
                UserProfile.objects.create(user=user, image=image)
            else:
                UserProfile.objects.create(user=user)
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'mainapp/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'mainapp/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

def posts_view(request):
    posts = Post.objects.select_related('author', 'author__user').order_by('-created_at')
    return render(request, 'mainapp/posts.html', {'posts': posts})

@login_required
def create_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = UserProfile.objects.get(user=request.user)
            post.save()
            return redirect('posts')
    else:
        form = PostForm()
    return render(request, 'mainapp/create_post.html', {'form': form})
@login_required
def edit_post_view(request, post_id):
    post = Post.objects.get(id=post_id)
    if post.author.user != request.user:
        return HttpResponseForbidden("Ви не можете редагувати цей пост.")

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form = PostForm(instance=post)

    return render(request, 'mainapp/edit_post.html', {'form': form, 'post': post})

@login_required
def delete_post_view(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        if post.author.user != request.user:
            return HttpResponseForbidden("Ви не можете видалити цей пост.")
        post.delete()
        return redirect('posts')
    except Post.DoesNotExist:
        raise Http404("Пост не знайдено")

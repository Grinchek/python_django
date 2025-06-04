from django.shortcuts import render

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

def about_view(request):
    return render(request, 'about.html')
def index_view(request):
    return render(request, 'index.html')

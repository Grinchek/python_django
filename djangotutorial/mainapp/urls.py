from django.urls import path
from .views import register_view, login_view, about_view, index_view

urlpatterns = [
    path('', index_view, name='index'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('about/', about_view, name='about'),
]
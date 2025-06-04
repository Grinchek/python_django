from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('about/', views.about_view, name='about'),
]

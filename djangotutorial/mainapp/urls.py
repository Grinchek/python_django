from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('about/', views.about_view, name='about'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('posts/', views.posts_view, name='posts'),
    path('posts/create/', views.create_post_view, name='create_post'),
    path('posts/edit/<int:post_id>/', views.edit_post_view, name='edit_post'),
    path('posts/delete/<int:post_id>/', views.delete_post_view, name='delete_post'),
]

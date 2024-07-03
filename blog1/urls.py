from django.urls import path
from django.contrib.auth import views as auth_views
from .views import post_list, post_detail, post_new, post_edit, post_delete, edit_profile, profile_view

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', post_list, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/new/', post_new, name='post_new'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', post_delete, name='post_delete'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/', profile_view, name='profile'),
]

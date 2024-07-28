from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, logout_view


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register', register, name='register'),
    path('logout', logout_view, name='logout'),
]
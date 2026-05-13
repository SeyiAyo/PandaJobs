from django.contrib import admin
from django.urls import path
from .views import frontpage, health_check, signup
from django.contrib.auth import views

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('health/', health_check, name='health_check'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
]

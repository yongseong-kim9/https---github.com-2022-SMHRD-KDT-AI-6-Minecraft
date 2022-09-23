from django.contrib import admin
from django.urls import path, include
from accounts import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('', views.index, name='index'),
    
]
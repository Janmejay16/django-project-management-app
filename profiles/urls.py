from django.urls import path, include

from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('register/', Register, name='register'),
    path('logout/', Logout, name='logout'),
    path('users/', UsersList, name='users'),
    path('user/<id>/', UserDetails, name='user'),
    path('user/delete/<int:pk>/', DeleteProfile.as_view(), name='delete'),
    path('user/edit/<int:pk>/', UpdateProfile.as_view(), name='edit'),
]

from django.urls import path
from .views import *

urlpatterns = [
    path('task/add/', TaskCreateView.as_view(), name='task'),
    path('tasks/', TasksList, name='tasks'),
    path('task/edit/<int:pk>/', TaskUpdateView.as_view(), name='edit'),
    path('task/delete/<int:pk>/', DeleteTask.as_view(), name='delete'),
    path('task/<int:pk>/', TaskDetails, name='task'),
]

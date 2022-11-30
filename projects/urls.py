from django.urls import path
from .views import *

urlpatterns = [
    path('project/add/', ProjectCreateView.as_view(), name='project'),
    path('projects/', ProjectsList, name='projects'),
    path('project/edit/<int:pk>/', ProjectUpdateView.as_view(), name='edit'),
    path('project/<int:pk>/', ProjectDetails, name='project'),
]

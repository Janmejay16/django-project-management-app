from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    path('admin/', admin.site.urls),
    path('', include(('profiles.urls', 'profiles'), namespace="profiles")),
    path('', include(('projects.urls', 'projects'), namespace="projects")),
    path('', include(('tasks.urls', 'tasks'), namespace="tasks")),
]

from django.urls import path
from .views import TasksHome


urlpatterns = [
    path('tasks/', TasksHome)
]

# http://localhost:8000/mytasksapp/     
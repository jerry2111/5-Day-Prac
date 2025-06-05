from django.urls import path
from . import views
urlpatterns = [
    path('tasks/', views.get_tasks, name='get_tasks'),
    path('tasks/create/', views.create_task, name='create_task'),
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
]
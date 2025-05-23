from django.urls import path
from task_manager.tasks import views


urlpatterns = [
    path('', views.TasksView.as_view(), name='tasks'),
    path('create/', views.TaskCreateView.as_view(), name='create_task'),
    path(
        '<int:pk>/update/',
        views.TaskUpdateView.as_view(),
        name='update_task'
    ),
    path(
        '<int:pk>/delete/',
        views.TaskDeleteView.as_view(),
        name='delete_task'
    ),
    path('<int:pk>/', views.TaskShowView.as_view(), name='show_task')
]

from django.urls import path
from task_manager.tasks import views


urlpatterns = [
    path('', views.Tasks.as_view(), name='tasks'),
    path('create/', views.TaskCreate.as_view(), name='create_task')
    # path('<int:id>/update/', views.UpdateStatus.as_view(), name='update_status'),
    # path('<int:id>/delete/', views.DeleteStatus.as_view(), name='delete_status')
]

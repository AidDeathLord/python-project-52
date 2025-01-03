from django.urls import path
from task_manager.statuses import views


urlpatterns = [
    path('', views.Statuses.as_view(), name='statuses'),
    path('create/', views.StatusCreate.as_view(), name='create_status'),
    path('<int:id>/update/', views.StatusUpdate.as_view(), name='update_status'),
    path('<int:id>/delete/', views.StatusDelete.as_view(), name='delete_status')
]

from django.urls import path
from task_manager.labels import views

urlpatterns = [
    path('', views.LabelsView.as_view(), name='labels'),
    path('create/', views.LabelsCreateView.as_view(), name='create_label'),
    path('<int:pk>/update/', views.LabelsUpdateView.as_view(), name='update_label'),
    path('<int:pk>/delete/', views.LabelsDeleteView.as_view(), name='delete_label')
]

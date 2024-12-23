from django.urls import path
from task_manager.users import views


urlpatterns = [
    path('', views.Users.as_view(), name='users'),
    path('create/', views.CreateUserView.as_view(), name='create_user'),
    path('<int:id>/update/', views.UpdateUserView.as_view(), name='update_user'),
    path('<int:id>/delete/', views.DeleteUserView.as_view(), name='delete_user')
]

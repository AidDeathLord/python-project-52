from django.urls import path
from task_manager.users import views


urlpatterns = [
    path('', views.Users.as_view(), name='users'),
    path('create/', views.CreateUser.as_view(), name='create_user')
]

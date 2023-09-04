from django.urls import path
from . import views

# urls
urlpatterns = [
    path('', views.home, name='home'),
    path('todo-list/', views.list_view, name='todo-list'),
    path('detail-view/<int:pk>/', views.detail_view, name='detail-view'),
    path('create-todo/', views.create_view, name='create-todo'),
    path('update-todo/<int:pk>/', views.update_view, name='update-todo'),
    path('delete-todo/<int:pk>/', views.delete_view, name='delete-todo'),

]

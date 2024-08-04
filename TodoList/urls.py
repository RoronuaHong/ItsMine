from django.urls import path
from TodoList import views

urlpatterns = [
  path('', views.render_todolist, name='todolist')
]

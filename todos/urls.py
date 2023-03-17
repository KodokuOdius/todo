from django.urls import path, include
from . import views

app_name = 'todos'
urlpatterns = [
    path('<int:pk>/', views.DetailTodo.as_view()),
    path('', views.ListTodo.as_view()),
]

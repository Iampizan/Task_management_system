from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'task_manager'

urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard", views.task_list, name="task_list"),
    path("task/new/", views.task_create, name="task_create"),
    path("task/<int:pk>/", views.task_detail, name="task_detail"),
    path("task/<int:pk>/edit/", views.task_update, name="task_update"),
    path("task/<int:pk>/delete/", views.task_delete, name="task_delete"),
    path("task/<int:pk>/complete/", views.mark_completed, name="mark_completed"),

]
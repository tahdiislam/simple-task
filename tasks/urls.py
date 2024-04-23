from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add_task, name="add_task"),
    path("all-tasks/", views.all_task, name="all_tasks"),
    path("edit-task/<int:id>", views.edit_task, name="edit_task"),
    path("delete-task/<int:id>", views.delete_task, name="delete_task"),
]

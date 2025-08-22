from django.contrib import admin
from django.urls import path
from . import views

from todo.views import TagsListView, TaskCreateView, TagsCreateView, TagUpdateView, TagDeleteView

app_name = "todo"

urlpatterns = [
    path("", views.index, name="index"),
    path("tags/", views.TagsListView.as_view(), name="tags"),
    path("tags/create/", views.TagsCreateView.as_view(), name="tags-create"),
    path("tags/<int:pk>/update/", views.TagUpdateView.as_view(), name="tags-update"),
    path("tags/<int:pk>/delete/", views.TagDeleteView.as_view(), name="tags-delete"),
    path("tasks/create/", views.TaskCreateView.as_view(), name="tasks-create"),
    path("tasks/<int:pk>/toggle/", views.toggle_task_status, name="tasks-toggle"),
]


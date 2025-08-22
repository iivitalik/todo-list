from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task, Tag




def index(request):
    tasks = Task.objects.all().order_by('-datetime')

    context = {
        'tasks': Task.objects.all()
    }
    return render(request, "index.html", context)


class TagsListView(ListView):
    model = Tag
    template_name = "tags.html"
    context_object_name = "tags"


class TaskCreateView(CreateView):
    model = Task
    fields = ("content", "deadline", "tags")
    success_url = reverse_lazy("todo:index")
    template_name = "tasks-create.html"


class TagsCreateView(CreateView):
    model = Tag
    fields = ("name", )
    success_url = reverse_lazy("todo:tags")
    template_name = "tags-create.html"


class TagUpdateView(UpdateView):
    model = Tag
    fields = ("name", )
    template_name = "tags-update.html"

    def get_success_url(self):
        return reverse_lazy("todo:tags")


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "tags-delete.html"

    def get_success_url(self):
        return reverse_lazy("todo:tags")


def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.done = not task.done
    task.save()
    return redirect("todo:index")
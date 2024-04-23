from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task


# Create your views here.
def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("all_tasks")
    else:
        form = TaskForm()
    return render(request, "tasks/add_task.html", {"form": form})


def all_task(request):
    data = Task.objects.all()
    return render(request, "tasks/all_task.html", {"data": data})


def edit_task(request, id):
    task = Task.objects.get(pk=id)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("all_tasks")
    return render(request, "tasks/edit_task.html", {"form": form})


def delete_task(request, id):
    Task.objects.get(pk=id).delete()
    return redirect("all_tasks")

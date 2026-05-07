from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Task
from .forms import TaskForm

User = get_user_model()


def home(request):
    return render(request, "task_manager/home_page.html")

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)

    todo_tasks = tasks.filter(status="TODO")
    progress_tasks = tasks.filter(status="IN_PROGRESS")
    completed_tasks = tasks.filter(status="COMPLETED")

    context = {
        "todo_tasks": todo_tasks,
        "progress_tasks": progress_tasks,
        "completed_tasks": completed_tasks,
    }
    return render(request, "task_manager/task_list.html", context)


@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    return render(request, "task_manager/task_details.html", {"task": task})


@login_required
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("task_manager:task_list")
    else:
        form = TaskForm()
    return render(request, "task_manager/task_form.html", {"form": form, "title": "Create Task"})


@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_manager:task_detail", pk=task.pk)
    else:
        form = TaskForm(instance=task)

    return render(request, "task_manager/task_form.html", {"form": form, "title": "Edit Task"})


@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == "POST":
        task.delete()
        return redirect("task_manager:task_list")

    return render(request, "task_manager/task_confirm_delete.html", {"task": task})


@login_required
def mark_completed(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == "POST" and task.status != "COMPLETED":
        task.status = "COMPLETED"
        task.save()

    return redirect("task_manager:task_list")
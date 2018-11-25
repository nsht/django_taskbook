import pdb

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import TodoItem, SubItem
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .forms import TodoItemForm

# Create your views here.


@login_required
def index(request):
    form = TodoItemForm()
    todos = TodoItem.objects.prefetch_related("subitem_set").all().filter(todo_user=request.user)
    context = {"todos": todos, "form": form}
    return render(request, "todo/index.html", context=context)


@login_required
def new_todo_page(request):
    form = TodoItemForm()

    return render(request, "todo/new_todo.html", {"form": form})


@login_required
def add_todo(request):
    todo_item = request.POST["todo_item"]
    new_todo = TodoItem.objects.create(
        todo_user=request.user, todo_item=todo_item, created=timezone.now(), status=0
    )
    new_todo.save()
    context = {"todo": new_todo}
    return render(request, "todo/single_todo.html", context)


@login_required
def toggle_completion(request):
    if request.POST["type"] == "subitem":
        todo = get_object_or_404(SubItem, id=request.POST["id"])
    else:
        todo = get_object_or_404(TodoItem, id=request.POST["id"])
    if not todo.todo_id.todo_user == request.user:
        return HttpResponse(status=401)
    if todo:
        if todo.status == 0:
            todo.status = 1
        else:
            todo.status = 0
        todo.save()
        return HttpResponse(status=200)


@login_required
def toggle_stars(request):
    todo = get_object_or_404(TodoItem, id=request.POST["id"])
    if not todo.todo_id.todo_user == request.user:
        return HttpResponse(status=401)
    if todo:
        if todo.starred == 0:
            todo.starred = 1
        else:
            todo.starred = 0
        todo.save()
        return HttpResponse(status=200)


@login_required
def new_sub_item(request):
    id = request.POST["todo_item_id"]
    id = id.split("_")[-1]
    todo = get_object_or_404(TodoItem, id=id, todo_user=request.user)
    sub_item = todo.subitem_set.create(
        sub_item=request.POST["sub_item"], sub_created=timezone.now()
    )
    print(sub_item)
    context = {"subitem": sub_item}
    return render(request, "todo/single_sub_item.html", context)
    # return HttpResponse(status=200)

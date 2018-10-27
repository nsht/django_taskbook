import pdb

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import TodoItem,SubItem
from django.utils import timezone

from .forms import TodoItemForm
# Create your views here.

def index(request):
    form = TodoItemForm()
    # todos = TodoItem.objects.all()
    todos = TodoItem.objects.prefetch_related('subitem_set').all()
    # todos[4].subitem_set.all()
    context = {
        'todos':todos,
        'form' : form
        }
    return render(request,'todo/index.html',context=context)

def new_todo(request):
    form = TodoItemForm()

    return render(request,'todo/new_todo.html', {'form': form})

def add_todo(request):
    print(request.POST)
    todo_item=request.POST['todo_item']
    print(todo_item)

    new_todo = TodoItem.objects.create(
        todo_item=todo_item,created=timezone.now(),status=0
        )
    new_todo.save()
    return HttpResponse(status=200)


def toggle_completion(request):
    if request.POST['type'] == 'subitem':
        todo = get_object_or_404(SubItem,id=request.POST['id'])
    else:
        todo = get_object_or_404(TodoItem,id=request.POST['id'])
    if todo:
        if todo.status == 0:
            todo.status = 1
        else:
            todo.status = 0
        todo.save()
        return HttpResponse(status=200)

def toggle_stars(request):
    todo = get_object_or_404(TodoItem,id=request.POST['id'])
    if todo:
        if todo.starred == 0:
            todo.starred = 1
        else:
            todo.starred = 0
        todo.save()
        return HttpResponse(status=200)

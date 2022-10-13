from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse, HttpResponseForbidden
from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos' : todos,
    }
    return render(request, 'todos/index.html', context)

def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.save()
        return redirect('todos:index')
    else:
        form = TodoForm()
    context = {
        'form':form,
    }
    return render(request, 'todos/create.html', context)

def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.user.is_authenticated:
        todo = Todo.objects.get(pk=pk)
        if request.user == todo.author:
            todo.delete()
            return redirect('todos:index')
    return redirect('todos:index', todo.pk)

def cancel(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.user.is_authenticated:
        todo = Todo.objects.get(pk=pk)
        if request.user == todo.author:
            todo.completed = 0
            todo.save()
            return redirect('todos:index')
    return redirect('todos:index', todo.pk)

def completed(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.user.is_authenticated:
        todo = Todo.objects.get(pk=pk)
        if request.user == todo.author:
            todo.completed = 1
            todo.save()
            return redirect('todos:index')
    return redirect('todos:index', todo.pk)
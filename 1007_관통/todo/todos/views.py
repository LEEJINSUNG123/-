from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe, require_http_methods, require_POST

from todos.forms import TodoForm
from .models import Todo


@require_safe   # get 방식
def index(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    # todos = Todo.objects.all()  # order_by 정렬해서 가졍ㅁ ( -pk ) = 내림차순
    todos = request.user.todo_set.all()
    context = {
        'todos' : todos,
    }
    return render(request, 'todos/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

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
        'form' : form,
    }
    return render(request, 'todos/create.html', context)

def toggle(request, pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    todo = Todo.objects.get(pk=pk)
    todo.completed = not todo.completed
    todo.save()
    
    return redirect('todos:index')

@require_POST
def delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    todo = Todo.objects.get(pk=pk)
    if request.user == todo.author:
        todo.delete()
    return redirect('todos:index')
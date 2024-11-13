from django.shortcuts import render, redirect
from django.http import HttpResponse
from .templates import *
from .models import *

# Create your views here.
'''def todoadd(request):
    return HttpResponse('<h1>This is TODO</h1>')'''


def todoadd(request):
    if request.method == 'POST':
        data = request.POST
        task = data.get('task')

        Todo.objects.create(task = task)
        return redirect('/todo/')
    
    queryset = Todo.objects.all()

    return render(request , 'todo.html', context={'queryset': queryset})


def edit_task(request, id):
    item = Todo.objects.get(id = id)
    if request.method == 'POST':
        data = request.POST
        update_task = data.get('task')

        item.task = update_task
        item.save()    
        return redirect('/todo/')

    queryset = item
    return render(request , 'update.html', context={'queryset': queryset})    

def delete_task(request, id):
    queryset = Todo.objects.get(id = id)
    queryset.delete()
    return redirect('/todo/')

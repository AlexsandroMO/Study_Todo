from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import Trata


@login_required
def taskList(request):

    user_login = Trata.read_sql2()
    print('\n\n\n')
    print('--------------->', user_login.username)
    print('\n\n\n')

    #who_login = Trata.read_sql3()
    #print('\n\n\n')
    #print('--------------->', who_login)
    #print('\n\n\n')

    search = request.GET.get('search')


    if search:
        tasks = Task.objects.filter(title__icontains=search)
    else:
        tasks_list = Task.objects.all().order_by('-create_at')
        paginator = Paginator(tasks_list, 6) #quantidde de linhas
        page = request.GET.get('page')
        tasks = paginator.get_page(page)

    return render(request, 'tasks/list.html', {'tasks': tasks})

@login_required
def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})

@login_required
def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            return redirect('/')

    else:
        form = TaskForm()
        return render(request, 'tasks/addtask.html', {'form': form})

@login_required
def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            task.save()
            return redirect('/')
        else:
            return render(request, 'tasks/edittask.html', {'form': form, 'task': task})

    else:
        return render(request, 'tasks/edittask.html', {'form': form, 'task': task})

@login_required
def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    messages.info(request, 'Tarefa deletada com sucesso.')
    return redirect('/')



#Testes
def yourName(request):

    return render(request, 'tasks/list.html', {'name': name})


def helloworld(request):
    return HttpResponse('Hello World!')






#@login_required
# def taskList(request):

#     search = request.GET.get('search')
#     if search:
#         tasks = Task.objects.filter(title__icontains=search)

#     else:

#         tasks_list = Task.objects.all().order_by('-create_at')

#         paginator = Paginator(tasks_list, 10) #quantidde de linhas

#         page = request.GET.get('page')

#         tasks = paginator.get_page(page)

#     return render(request, 'tasks/list.html', {'tasks': tasks})

# #@login_required
# def newTask(request):
#     if request.method == 'POST':
#         form = TaskForm(request.POST)

#         if form.is_valid():
#             task = form.save(commit=False)
#             task.done = 'doing'
#             task.save()
#             return redirect('/')

#     else:
#         form = TaskForm()
#         return render(request, 'tasks/addtask.html', {'form': form})

#     form = TaskForm()
#     return render(request, 'tasks/addtask.html', {'form': form})

# #@login_required
# def editTask(request, id):
#     task = get_object_or_404(Task, pk=id)
#     form = TaskForm(instance=task)

#     if request.method == 'POST':
#         form = TaskForm(request.POST, instance=task)

#         if form.is_valid():
#             task.save()
#             return redirect('/')
#         else:
#             return render(request, 'tasks/edittask.html', {'form': form, 'ask': task})

#     else:
#         return render(request, 'tasks/edittask.html', {'form': form, 'ask': task})

# #@login_required
# def deleteTask(request, id):
#     task = get_object_or_404(Task, pk=id)
#     task.delete()

#     messages.info(request, 'Tarefa deletada com sucesso.')
#     return redirect('/')

# #@login_required
# def taskView(request, id):
#     task = get_object_or_404(Task, pk=id)
#     return render(request, 'tasks/task.html', {'task': task})


from django.shortcuts import render,redirect
from to_do.forms import TaskForm
from to_do.models import TaskModel
# Create your views here.


def home(request):
    return render(request, "home.html")


def add_task(request):
    if request.method == "POST":
        task = TaskForm(request.POST)   
        if task.is_valid():
            task.save()
            print(task.cleaned_data)
            return redirect(show_tasks)
    else :
        task = TaskForm()
    return render(request,"add_task.html", {'form':task})


def show_tasks(request):
    tasks = TaskModel.objects.all()
    return render(request,"show_tasks.html",{'tasks':tasks})


def edit_task(request,id):
    tasks = TaskModel.objects.get(pk=id)
    task = TaskForm(instance=tasks)
    if request.method == "POST":
        task = TaskForm(request.POST,instance=tasks)
        if task.is_valid():
            task.save()
            print(task.cleaned_data)
            return redirect(show_tasks)
    return render(request,"add_task.html", {'form':task})


def delete_task(request,id):
    task = TaskModel.objects.get(pk=id).delete()
    return redirect(show_tasks)


def complete_task(request,id):
    tasks = TaskModel.objects.get(pk=id)
    tasks.completed = True
    tasks.save()
    return redirect("completed_tasks")


def completed_tasks(request):
    tasks = TaskModel.objects.filter(completed=True)
    return render(request,"completed_tasks.html",{"tasks":tasks})



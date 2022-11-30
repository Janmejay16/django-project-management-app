from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Task
from profiles.models import Profile
from django.urls import reverse_lazy
from .forms import *

# Create your views here.

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskCreationForm
    success_url = reverse_lazy('tasks:tasks')
    template_name = 'add.html'

    def get_form_kwargs(self):
        kw = super(TaskCreateView, self).get_form_kwargs()
        kw['request'] = self.request # the trick!
        return kw

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskUpdationForm
    success_url = reverse_lazy('profiles:dashboard')
    template_name = 'edit.html'

def TasksList(request):
    tasks = Task.objects.all()
    edit = True

    if (request.session['userdata']['role'] == 'manager'):
        edit = True
        tasks = Profile.objects.get(id=request.session['userdata']['id']).my_tasks.all()

    if (request.session['userdata']['role'] == 'member'):
        edit = False
        tasks = Profile.objects.get(id=request.session['userdata']['id']).enrolled_tasks.all()

    return render(request, 'tasks.html', {"data": {"tasks": tasks, "edit": edit}})



def TaskDetails(request, pk):
    status = {
        "not started": "danger",
        "in progress": "warning",
        "completed": "info",
        "in review": "secondary",
        "closed": "success"
    }
    task = Task.objects.get(id=pk)
    project = Project.objects.get(id=task.project.id)
    if request.session['userdata']:
        user = Profile.objects.get(id=request.session['userdata']['id'])
        if (
            request.session['userdata']['role'] == 'manager' or
            request.session['userdata']['role'] == 'member'
        ):
            if(
                user in project.managers.all() or
                user in task.assigned_to.all()
            ):
                return render(request, 'task.html', {"data": {"task": task, "edit": True, "status": status[task.status.lower()], "managers": project.managers.all}})

    else:
        return render(request, 'task.html', {"data": {"task": task, "edit": False, "status": status[task.status.lower()], "managers": project.managers.all}})

    return render(request, 'task.html', {"data": {"task": task, "edit": False, "status": status[task.status.lower()], "managers": project.managers.all}})


class DeleteTask(DeleteView):
    print('Hey')
    model = Task
    template_name = 'delete_task.html'
    success_url = reverse_lazy('profiles:dashboard')
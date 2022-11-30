from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from .models import Project
from profiles.models import Profile
from django.urls import reverse_lazy
from .forms import *

# Create your views here.

class ProjectCreateView(CreateView):
    model = Project
    success_url = reverse_lazy('projects:projects')
    fields=['name','start_date', 'end_date','description']
    template_name = 'add.html'

    def form_valid(self, form):
        self.object = form.save()
        project = Project.objects.get(id=self.object.get_id())
        project.managers.add(Profile.objects.get(id=self.request.session['userdata']['id']))
        return HttpResponseRedirect(self.get_success_url())

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectUpdationForm
    success_url = reverse_lazy('profiles:dashboard')
    template_name = 'edit.html'

def ProjectsList(request):
    projects = Project.objects.all()
    edit = True

    if (request.session['userdata']['role'] == 'manager'):
        edit = True
        projects = Profile.objects.get(id=request.session['userdata']['id']).my_projects.all()

    if (request.session['userdata']['role'] == 'member'):
        edit = False
        projects = Profile.objects.get(id=request.session['userdata']['id']).enrolled_projects.all()

    return render(request, 'projects.html', {"data": {"projects": projects, "edit": edit}})



def ProjectDetails(request, pk):
    project = Project.objects.get(id=pk)
    print(project)
    if request.session['userdata']:
        user = Profile.objects.get(id=request.session['userdata']['id'])
        if (request.session['userdata']['role'] == 'manager'):
            if(user in project.managers.all()):
                return render(request, 'project.html', {"data": {"project": project, "edit": True}})

    else:
        return render(request, 'project.html', {"data": {"project": project, "edit": False}})

    return render(request, 'project.html', {"data": {"project": project, "edit": False}})



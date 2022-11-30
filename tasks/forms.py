from django.forms import *
from profiles.models import Profile
from projects.models import Project
from .models import Task

class TaskCreationForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(TaskCreationForm, self).__init__(*args, **kwargs)
        id = self.request.session['userdata']['id']
        user = Profile.objects.get(id=id)

        projects = Project.objects.filter(pk__in=user.my_projects.all())

        self.fields['creator'] = ModelChoiceField(
            queryset=Profile.objects.filter(id=id),
        )
        self.fields['project'] = ModelChoiceField(
            queryset=projects,
        )

    class Meta:
        model = Task
        fields=['name', 'status', 'start_time', 'finish_time','description', 'project','creator']

class TaskUpdationForm(ModelForm):

    def __init__(self, *args, **kwargs):
        task = Task.objects.get(id = kwargs['instance'].id)
        project = Project.objects.get(id=task.project.id)
        super(TaskUpdationForm, self).__init__(*args, **kwargs)

        self.fields['assigned_to'] = ModelMultipleChoiceField(
            queryset=project.members,
            widget = CheckboxSelectMultiple()
        )

    class Meta:
        model = Task
        fields=['name', 'status', 'start_time', 'finish_time','description', 'assigned_to']

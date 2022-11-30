from django.forms import *
from profiles.models import Profile
from .models import Project

class ProjectUpdationForm(ModelForm):

    def __init__(self, *args, **kwargs):
        managers = Profile.objects.filter(role='manager')
        members = Profile.objects.filter(role='member')
        super(ProjectUpdationForm, self).__init__(*args, **kwargs)
        self.fields['managers'] = ModelMultipleChoiceField(
            queryset=managers,
            widget = CheckboxSelectMultiple()
        )

        self.fields['members'] = ModelMultipleChoiceField(
            queryset=members,
            widget = CheckboxSelectMultiple()
        )

    class Meta:
        model = Project
        fields=['name','start_date', 'end_date','description', 'members', 'managers']

from django.db import models

# Create your models here.
from django.db.models import *
from profiles.models import Profile
from projects.models import Project
from datetime import datetime

class Task(Model):

    task_status = [
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('In Review', 'In Review'),
        ('Closed', 'Closed'),
    ]

    name = CharField(max_length=100)
    budget = PositiveBigIntegerField(default=0)
    assigned_to = ManyToManyField(Profile, name='assigned_to', related_name='tasks_assigned', null=True, blank=True)
    created_by = ForeignKey(Profile, name='creator', related_name='my_tasks', on_delete=CASCADE)
    project = ForeignKey(Project, on_delete=CASCADE, related_name='tasks')
    start_time = DateTimeField(default=datetime.now, blank=True)
    finish_time = DateTimeField(null=True, blank=True)
    description = TextField(blank=True, default='')
    status = CharField(choices=task_status, max_length=20, default='Not Started')
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_id(self):
        return self.id
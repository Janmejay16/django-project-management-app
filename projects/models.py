from django.db import models
from profiles.models import Profile
from datetime import datetime

class Project(models.Model):
    name = models.CharField(max_length=100)
    budget = models.PositiveBigIntegerField(default=0)
    members = models.ManyToManyField(Profile, name='members', related_name='enrolled_projects', null=True, blank=True)
    managers = models.ManyToManyField(Profile, name='managers', related_name='my_projects', null=True, blank=True)
    start_date = models.DateField(default=datetime.now, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_id(self):
        return self.id
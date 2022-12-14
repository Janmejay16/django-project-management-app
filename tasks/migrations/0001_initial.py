# Generated by Django 4.1.3 on 2022-11-29 22:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('budget', models.PositiveBigIntegerField(default=0)),
                ('start_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('finish_time', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(blank=True, default='')),
                ('status', models.CharField(choices=[('Not Started', 'Not Started'), ('In Progress', 'In Progress'), ('Completed', 'Completed'), ('In Review', 'In Review'), ('Closed', 'Closed')], default='Not Started', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('assigned_to', models.ManyToManyField(blank=True, null=True, related_name='tasks_assigned', to='profiles.profile')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_tasks', to='profiles.profile')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]

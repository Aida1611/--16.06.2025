from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    time = models.TimeField()
    date = models.DateField()

    def __str__(self):
        return self.title

class Programmer(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    group = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Task(models.Model):
    LEVEL_CHOICES = [
        ('easy', 'Жеңил'),
        ('medium', 'Орточо'),
        ('hard', 'Оор'),
        ('very_hard', 'Өтө оор'),
    ]
    STATUS_CHOICES = [
        ('task', 'Task'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]
    title = models.CharField(max_length=100)
    name_task = models.CharField(max_length=100)
    deadline = models.DateField()
    programmer = models.ForeignKey(Programmer, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='easy')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='task')

    def __str__(self):
        return self.title

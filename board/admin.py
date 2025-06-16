from django.contrib import admin
from .models import Project, Programmer, Task

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time')

@admin.register(Programmer)
class ProgrammerAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'group')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'status', 'deadline', 'programmer', 'project')
    list_filter = ('level', 'status')
    search_fields = ('title', 'name_task')

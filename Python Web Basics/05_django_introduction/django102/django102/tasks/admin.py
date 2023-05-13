from django.contrib import admin

from django102.tasks.models import Task


# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'task_title', 'task_text')

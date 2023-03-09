from django.contrib import admin

# Register your models here.

from .models import Task, TaskDate, History

admin.site.register(Task)
admin.site.register(TaskDate)
admin.site.register(History)

from django.contrib import admin

from Task.models import Tag, Task

admin.site.register(Tag)
admin.site.register(Task)
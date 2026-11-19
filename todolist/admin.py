from django.contrib import admin
from todolist.models import Task
from .models import  ContactMessage

admin.site.register(Task)
admin.site.register(ContactMessage)

from django.contrib import admin
from .models import Column, Task


@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'status', 'column', 'created_at')
    search_fields = ('description', 'status')
    list_filter = ('status', 'column')


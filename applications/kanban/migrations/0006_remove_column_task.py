# Generated by Django 5.1.3 on 2024-11-22 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0005_rename_tasks_column_task_alter_task_column'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='column',
            name='task',
        ),
    ]

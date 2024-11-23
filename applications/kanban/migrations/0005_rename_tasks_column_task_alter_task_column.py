# Generated by Django 5.1.3 on 2024-11-22 12:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0004_remove_column_task_column_tasks_alter_task_column'),
    ]

    operations = [
        migrations.RenameField(
            model_name='column',
            old_name='tasks',
            new_name='task',
        ),
        migrations.AlterField(
            model_name='task',
            name='column',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='kanban.column'),
        ),
    ]

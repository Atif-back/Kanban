# Generated by Django 5.1.3 on 2024-11-22 11:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0002_alter_task_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='column',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='kanban.column'),
        ),
    ]

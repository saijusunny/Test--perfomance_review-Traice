# Generated by Django 4.0.2 on 2023-02-18 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_performance_workdetails'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='emp_id',
            new_name='assign_emp_id',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='note',
            new_name='person_id',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='name',
        ),
    ]

# Generated by Django 4.0.2 on 2023-02-18 05:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_rename_request_money'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('emp_id', models.CharField(max_length=100)),
                ('note', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='performance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=100)),
                ('emp_id', models.CharField(max_length=100)),
                ('percentage', models.CharField(max_length=100)),
                ('date', models.DateField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='post',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('STAFF', 'Staff'), ('USERS', 'Users')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='salary',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('STAFF', 'Staff'), ('USERS', 'Users')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='money',
        ),
        migrations.DeleteModel(
            name='transaction',
        ),
        migrations.AddField(
            model_name='performance',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feedback',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

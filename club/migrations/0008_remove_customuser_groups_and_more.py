# Generated by Django 4.1.2 on 2023-10-01 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0007_customuser_groups_customuser_is_superuser_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='user_permissions',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

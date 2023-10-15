# Generated by Django 4.1.2 on 2023-10-02 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0012_customuser_delete_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]

# Generated by Django 2.2.5 on 2021-02-18 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_management', '0002_task_has_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_type',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='project_type',
            name='date_modified',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='date_deleted',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='date_modified',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='resource_type',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='resource_type',
            name='date_modified',
            field=models.DateField(auto_now=True),
        ),
    ]
# Generated by Django 4.0.5 on 2022-06-19 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_rename_url_project_info'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='info',
            new_name='imfo',
        ),
    ]

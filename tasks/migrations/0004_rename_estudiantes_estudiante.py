# Generated by Django 4.2.4 on 2023-08-27 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='estudiantes',
            new_name='estudiante',
        ),
    ]

# Generated by Django 4.2.4 on 2023-09-03 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_rename_nombre_estudiante_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='codigo',
            field=models.CharField(unique=True),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='password',
            field=models.CharField(),
        ),
    ]

# Generated by Django 4.1.7 on 2023-05-22 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloc', '0009_alter_project_date_debut_alter_project_date_fin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='date_debut',
            new_name='datedebut',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='date_fin',
            new_name='datefin',
        ),
    ]
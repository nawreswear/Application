# Generated by Django 4.1.7 on 2023-05-22 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloc', '0003_project_date_debut_project_date_fin_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='date_debut',
        ),
        migrations.RemoveField(
            model_name='project',
            name='date_fin',
        ),
    ]
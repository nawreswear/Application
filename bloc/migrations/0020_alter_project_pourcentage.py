# Generated by Django 4.2.1 on 2023-05-22 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloc', '0019_alter_project_date_debut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='pourcentage',
            field=models.PositiveIntegerField(),
        ),
    ]

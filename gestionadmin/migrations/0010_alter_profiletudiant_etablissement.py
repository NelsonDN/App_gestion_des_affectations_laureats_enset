# Generated by Django 5.0.3 on 2024-05-17 22:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0009_alter_profiletudiant_etablissement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiletudiant',
            name='etablissement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionadmin.etablissement'),
        ),
    ]

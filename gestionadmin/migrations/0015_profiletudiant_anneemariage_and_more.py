# Generated by Django 5.0.3 on 2024-06-05 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0014_profiletudiant_is_visible'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiletudiant',
            name='anneeMariage',
            field=models.DateField(blank=True, null=True, verbose_name='Année mariage civil'),
        ),
        migrations.AddField(
            model_name='profiletudiant',
            name='estEffectif',
            field=models.DateField(blank=True, null=True, verbose_name='Prise effective Mari valide ?'),
        ),
    ]

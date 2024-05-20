# Generated by Django 5.0.3 on 2024-05-17 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0005_alter_ddepartement_options_alter_dregion_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='besoineffectif',
            name='etablissement',
        ),
        migrations.RemoveField(
            model_name='besoineffectif',
            name='filiere',
        ),
        migrations.RemoveField(
            model_name='filiere',
            name='cycle',
        ),
        migrations.RemoveField(
            model_name='ddepartement',
            name='region',
        ),
        migrations.RemoveField(
            model_name='etablissement',
            name='departement',
        ),
        migrations.RemoveField(
            model_name='filiere',
            name='departement',
        ),
        migrations.RemoveField(
            model_name='profiletudiant',
            name='etablissement',
        ),
        migrations.RemoveField(
            model_name='profiletudiant',
            name='filiere',
        ),
        migrations.RemoveField(
            model_name='profiletudiant',
            name='user',
        ),
        migrations.DeleteModel(
            name='Etudiant',
        ),
        migrations.DeleteModel(
            name='BesoinEffectif',
        ),
        migrations.DeleteModel(
            name='Cycle',
        ),
        migrations.DeleteModel(
            name='DRegion',
        ),
        migrations.DeleteModel(
            name='DDepartement',
        ),
        migrations.DeleteModel(
            name='Departement',
        ),
        migrations.DeleteModel(
            name='Etablissement',
        ),
        migrations.DeleteModel(
            name='Filiere',
        ),
        migrations.DeleteModel(
            name='ProfilEtudiant',
        ),
    ]

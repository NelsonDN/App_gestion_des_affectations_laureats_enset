# Generated by Django 5.0.3 on 2024-05-17 18:00

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('gestionadmin', '0003_alter_besoineffectif_etablissement'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Etudiant',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='besoineffectif',
            name='nombreEffectif',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name="Nombre d'effectif "),
        ),
        migrations.CreateModel(
            name='ProfilEtudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rang', models.IntegerField(blank=True, null=True, verbose_name='Rang promotion')),
                ('dateNaissance', models.DateField(blank=True, null=True, verbose_name='Date de naissance')),
                ('anneeSortie', models.DateField(verbose_name='Année de sortie')),
                ('matricule', models.CharField(max_length=64, unique=True, verbose_name='Matricule')),
                ('telephone', models.CharField(blank=True, max_length=64, null=True, verbose_name='Numéro de télephone')),
                ('sexe', models.CharField(blank=True, max_length=64, null=True, verbose_name='Sexe')),
                ('etablissement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionadmin.etablissement')),
                ('filiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionadmin.filiere')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profil Etudiant',
                'verbose_name_plural': 'Profil Etudiants',
            },
        ),
    ]
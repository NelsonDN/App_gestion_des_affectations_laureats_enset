# Generated by Django 5.0.3 on 2024-05-17 23:39

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('gestionadmin', '0011_remove_besoineffectif_departement_and_more'),
        ('gestiondelegation', '0001_initial'),
        ('gestionetablissement', '0001_initial'),
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
        migrations.CreateModel(
            name='Etablissement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Nom')),
                ('BP', models.CharField(blank=True, max_length=64, null=True, verbose_name='BP')),
                ('email', models.CharField(max_length=64, unique=True, verbose_name='email')),
                ('departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestiondelegation.ddepartement', verbose_name='Departement')),
            ],
            options={
                'verbose_name': 'Etablissement',
                'verbose_name_plural': 'Etablissements',
            },
        ),
        migrations.CreateModel(
            name='BesoinEffectif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreEffectif', models.IntegerField(blank=True, default=0, null=True, verbose_name="Nombre d'effectif ")),
                ('departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionetablissement.departement')),
                ('etablissement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionadmin.etablissement')),
            ],
            options={
                'verbose_name': "Besoin d'effectif",
                'verbose_name_plural': "Besoin d'effectifs",
            },
        ),
        migrations.CreateModel(
            name='Filiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Nom')),
                ('cycle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionetablissement.cycle')),
                ('departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionetablissement.departement')),
            ],
            options={
                'verbose_name': 'Filière',
                'verbose_name_plural': 'Filières',
            },
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
                ('sexe', models.CharField(blank=True, choices=[('M', 'Masculin'), ('F', 'Féminin')], max_length=64, null=True, verbose_name='Sexe')),
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

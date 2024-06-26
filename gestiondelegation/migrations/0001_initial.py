# Generated by Django 5.0.3 on 2024-05-17 23:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DRegion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Nom')),
            ],
            options={
                'verbose_name': 'Délégation Régionale',
                'verbose_name_plural': 'Délégations Régionale',
            },
        ),
        migrations.CreateModel(
            name='DDepartement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Nom')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestiondelegation.dregion')),
            ],
            options={
                'verbose_name': 'Délégation Départementale',
                'verbose_name_plural': 'Délégations Départementale',
            },
        ),
    ]

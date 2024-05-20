from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from datetime import date
from gestiondelegation.models import DRegion, DDepartement
from gestionetablissement.models import Cycle, Departement
from django.contrib.auth.hashers import make_password

class Etablissement(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name= "Nom")
    BP = models.CharField(max_length=64, null=True, blank=True, verbose_name= "BP")
    email = models.CharField(max_length=64, unique=True, verbose_name= "email")
    departement = models.ForeignKey(DDepartement, on_delete=models.CASCADE, verbose_name= "Departement")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Etablissement"
        verbose_name_plural = "Etablissements"

class Filiere(models.Model):
    name = models.CharField(max_length=64, verbose_name= "Nom")
    cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)

    def __str__(self):
        valeur = self.name  or ""
        return f"{valeur} ({self.cycle.name}) - {self.departement.name}".strip()
    
    class Meta:
        verbose_name = "Filière"
        verbose_name_plural = "Filières"

class BesoinEffectif(models.Model):
    nombreEffectif = models.IntegerField(default=0, null=True, blank=True, verbose_name= "Nombre d'effectif ")
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    etablissement = models.ForeignKey(Etablissement, on_delete=models.CASCADE)

    def __str__(self):
        valeur = self.departement.name  or ""
        return f"{valeur} - {self.etablissement.name}".strip()
    
    class Meta:
        verbose_name = "Besoin d'effectif"
        verbose_name_plural = "Besoin d'effectifs"

class Etudiant(User):
    class Meta:
        proxy = True

    def __str__(self):
        valeur = self.username  or ""
        return  f"{valeur}".strip()

class ProfilEtudiant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)
    rang = models.IntegerField(null=True, blank=True, verbose_name= "Rang promotion")
    dateNaissance = models.DateField(null=True, blank=True, verbose_name= "Date de naissance")
    anneeSortie = models.DateField(verbose_name= "Année de sortie")
    matricule = models.CharField(max_length=64, unique=True, verbose_name= "Matricule")
    telephone = models.CharField(max_length=64, null=True, blank=True, verbose_name= "Numéro de télephone")
    sexes = [('M', 'Masculin'), ('F', "Féminin")]
    sexe = models.CharField(max_length=64, choices=sexes, null=True, blank=True, verbose_name= "Sexe")
    etablissement = models.ForeignKey(Etablissement, null=True, blank=True, on_delete=models.CASCADE)
    is_visible = models.BooleanField(default=False, null=True, blank=True,)

    def __str__(self):
        valeur = self.matricule  or ""
        return  f"{valeur} - {self.user.username}".strip()
    
    class Meta:
        verbose_name = "Profil Etudiant"
        verbose_name_plural = "Profil Etudiants"


class Choix(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    choix1 = models.ForeignKey(DRegion, on_delete=models.CASCADE, null=True, blank=True, related_name='choix1')
    choix2 = models.ForeignKey(DRegion, on_delete=models.CASCADE, null=True, blank=True, related_name='choix2')
    choix3 = models.ForeignKey(DRegion, on_delete=models.CASCADE, null=True, blank=True, related_name='choix3')
    choix4 = models.ForeignKey(DRegion, on_delete=models.CASCADE, null=True, blank=True, related_name='choix4')
    choix5 = models.ForeignKey(DRegion, on_delete=models.CASCADE, null=True, blank=True, related_name='choix5')
    choix6 = models.ForeignKey(DRegion, on_delete=models.CASCADE, null=True, blank=True, related_name='choix6')
    choix7 = models.ForeignKey(DRegion, on_delete=models.CASCADE, null=True, blank=True, related_name='choix7')
    choix8 = models.ForeignKey(DRegion, on_delete=models.CASCADE, null=True, blank=True, related_name='choix8')
    choix9 = models.ForeignKey(DRegion, on_delete=models.CASCADE, null=True, blank=True, related_name='choix9')
    choix10 = models.ForeignKey(DRegion, on_delete=models.CASCADE, null=True, blank=True, related_name='choix10')

    def __str__(self):
        return  f"{self.user.username}".strip()
    
    class Meta:
        verbose_name = "Choix"
        verbose_name_plural = "Choix"

# Pour éviter les appels récursifs
updating_user = False

@receiver(post_save, sender=ProfilEtudiant)
def set_default_password(sender, instance, created, **kwargs):
    global updating_user
    if created and not updating_user:
        user = instance.user
        matricule = instance.matricule
        if matricule:
            hashed_password = make_password(matricule)
            updating_user = True
            User.objects.filter(pk=user.pk).update(password=hashed_password)
            updating_user = False

# @receiver(post_save, sender=ProfilEtudiant)
# def set_default_password(sender, instance, created, **kwargs):
#     user = instance.user
#     matricule = instance.matricule
#     if matricule and created:
#         hashed_password = make_password(matricule)
#         User.objects.filter(pk=user.pk).update(password=hashed_password)

# @receiver(pre_save, sender=User)
# def handle_profile_pre_update(sender, instance, **kwargs):
#     # instance.set_password("matricule")
#     # instance.save()
#     hashed_password = make_password("matricule")
#     User.objects.filter(pk=instance.pk).update(password=hashed_password)

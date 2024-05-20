from django.db import models

class Cycle(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name= "Nom")

    def __str__(self):
        valeur = self.name  or ""
        return  f"{valeur}".strip()
    
    class Meta:
        verbose_name = "Cycle"
        verbose_name_plural = "Cycles"

class Departement(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name= "Nom")

    def __str__(self):
        valeur = self.name  or ""
        return  f"{valeur}".strip()
    
    class Meta:
        verbose_name = "Departement"
        verbose_name_plural = "Departements"



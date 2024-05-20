from django.db import models

# Create your models here.


class DRegion(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name= "Nom")

    def __str__(self):
        valeur = self.name  or ""
        return  f"{valeur}".strip()
    
    class Meta:
        verbose_name = "Délégation Régionale"
        verbose_name_plural = "Délégations Régionale"

class DDepartement(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name= "Nom")
    region = models.ForeignKey(DRegion, on_delete=models.CASCADE)

    def __str__(self):
        valeur = self.name  or ""
        return  f"{valeur}".strip()
    
    class Meta:
        verbose_name = "Délégation Départementale"
        verbose_name_plural = "Délégations Départementale"
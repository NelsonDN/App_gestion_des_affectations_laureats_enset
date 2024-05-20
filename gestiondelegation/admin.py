from django.contrib import admin
from .models import DRegion, DDepartement
from django.utils.html import format_html

@admin.register(DRegion)
class DRegionAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('name',)
    list_filter = ['name']
    search_fields = ['name']
    list_per_page = 10
    

@admin.register(DDepartement)
class DDepartementAdmin(admin.ModelAdmin):
    fields = ['name', 'region']
    list_display = ('name', 'region', 'Liste_des_etablissements')
    list_filter = ['name', 'region__name']
    search_fields = ['name']
    list_per_page = 15

    def Liste_des_etablissements(self, obj):
        return format_html('<a href="/admin/gestionadmin/etablissement/?departement__id__exact={}">Consulter</a>'.format(obj.id))
    Liste_des_etablissements.allow_tags = True
    Liste_des_etablissements.short_description = "Liste des Etablissements"


from django.contrib import admin
from .models import  Cycle, Departement
from gestionadmin.admin import FiliereInline


@admin.register(Cycle)
class CycleAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('name',)
    list_filter = ['name']
    search_fields = ['name']
    list_per_page = 10

@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('name',)
    list_filter = ['name']
    search_fields = ['name']
    list_per_page = 10
    
    inlines = [FiliereInline]
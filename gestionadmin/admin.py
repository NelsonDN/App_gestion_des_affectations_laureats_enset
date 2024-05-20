from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import DRegion, DDepartement, Cycle, Departement, Filiere, Etablissement, BesoinEffectif, Etudiant, ProfilEtudiant
from .forms import EtudiantCreationForm, ProfileEtudiantForm
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from .views import lancer_affectation

class FiliereInline(admin.TabularInline):
    model = Filiere

class BesoinEffectifInline(admin.TabularInline):
    model = BesoinEffectif

class ProfileInline(admin.StackedInline):
    form = ProfileEtudiantForm
    model = ProfilEtudiant

@admin.register(Etablissement)
class EtablissementAdmin(admin.ModelAdmin):
    fields = ['name', 'BP', 'email', 'departement']

    list_display = ('name', 'BP', 'email', 'departement')
    list_filter = ['name', 'departement']
    search_fields = ['departement__name', 'name']
    list_per_page = 10

    inlines = [BesoinEffectifInline]

    # def Gerer_les_postes(self, obj):
    #     return format_html('<a href="/admin/gestionministere/etablissement_poste/?etablissement__id__exact={}">Gérer les postes</a>'.format(obj.id))
    # Gerer_les_postes.allow_tags = True
    # Gerer_les_postes.short_description = "Gérer les postes"

    # def Gerer_les_enseignants(self, obj):
    #     return format_html('<a href="/admin/gestionministere/profilenseignant/?etablissement__id__exact={}">Consulter</a>'.format(obj.id))
    # Gerer_les_enseignants.allow_tags = True
    # Gerer_les_enseignants.short_description = "Liste Enseignant"



class EtudiantAdmin(admin.ModelAdmin):
    form = EtudiantCreationForm

    def custom_action(modeladmin, request, queryset):
        for obj in queryset:
            lancer_affectation(obj)
        
        modeladmin.message_user(request, "Le Processus d'affectation a été exécutée avec succès!")

    custom_action.short_description = "LANCER LE PROCESSUS D'AFFECTATION"
    actions = [custom_action]

    list_display = ('nom_etudiant', 'email', 'matricule', 'filiere')
    inlines = [ProfileInline]

    # def get_form(self, request, obj=None, **kwargs):
    #     if obj:  # Vérifie si un objet est en cours d'édition
    #         return EnseignantEditForm
    #     return super().get_form(request, obj, **kwargs)
    
    # def Consulter_carriere(self, obj):
    #     return format_html('<a href="/admin/gestionministere/carriere/?user__id__exact={}">Consulter</a>'.format(obj.id))
    # Consulter_carriere.allow_tags = True
    # Consulter_carriere.short_description = "Historique carrière"

    def nom_etudiant(self, obj):
        return obj.username
    
    def filiere(self, obj):
        return obj.profiletudiant.filiere
    
    def matricule(self, obj):
        # profil = ProfilEtudiant.objects.get(user=obj)
        return obj.profiletudiant.matricule
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_superuser=False)

admin.site.register(Etudiant, EtudiantAdmin)

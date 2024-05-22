from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import DRegion, DDepartement, Cycle, Departement, Filiere, Etablissement, BesoinEffectif, Etudiant, ProfilEtudiant
from .forms import EtudiantCreationForm, ProfileEtudiantForm
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from .views import lancer_affectation
from import_export import resources, fields
from import_export.admin import ExportActionMixin, ImportMixin
from reportlab.pdfgen import canvas
from django.http import HttpResponse

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

# class EtudiantResource(resources.ModelResource):
#     def get_export_fields(self):
#             fields = ['nom_etudiant', 'email', 'matricule', 'filiere']
#             if ProfilEtudiant.objects.exclude(etablissement=None).exists():
#                 fields.append('etablissement')
#             return fields
#     class Meta:
#         model = Etudiant

class EtudiantResource(resources.ModelResource):
    class Meta:
        model = Etudiant
        fields = ('nom_etudiant', 'email', 'matricule', 'filiere', 'etablissement')
        import_id_fields = ['nom_etudiant']  # Champs utilisés pour l'identification des enregistrements lors de l'importation

# class EtudiantResource(resources.ModelResource):
#     class Meta:
#         model = Etudiant
#         fields = ('nom_etudiant', 'email', 'matricule', 'filiere')  # Spécifiez les champs à exporter
#         export_order = fields  # Ordre dans lequel les champs seront exportés

        
# class EtudiantResource(resources.ModelResource):
#     # Définir les champs à exporter
#     nom_etudiant = fields.Field(attribute='username', column_name='Nom')
#     email = fields.Field(attribute='email', column_name='Email')
#     matricule = fields.Field(attribute='profiletudiant__matricule', column_name='Matricule')
#     filiere = fields.Field(attribute='profiletudiant__filiere', column_name='Filière')
#     etablissement = fields.Field(attribute='profiletudiant__etablissement', column_name="Etablissement d'Affectation")

#     class Meta:
#         model = Etudiant
#         # Définir les champs à exporter
#         fields = ('nom_etudiant', 'email', 'matricule', 'filiere', 'etablissement')
#         export_fields = fields
#     def dehydrate_etablissement(self, etudiant):
#         # Fonction pour extraire la valeur du champ 'etablissement' de ProfilEtudiant
#         return etudiant.profiletudiant.etablissement if etudiant.profiletudiant.etablissement else ""

class EtudiantAdmin(ExportActionMixin, ImportMixin, admin.ModelAdmin):
    form = EtudiantCreationForm
    resource_class = EtudiantResource

  
    list_display = ('nom_etudiant', 'email', 'matricule', 'filiere')


    def custom_action(modeladmin, request, queryset):
        for obj in queryset:
            lancer_affectation(obj)
        
        modeladmin.message_user(request, "Le Processus d'affectation a été exécutée avec succès!")
    custom_action.short_description = "LANCER LE PROCESSUS D'AFFECTATION"



    def export_pdf(self, request, queryset):
        # Créer une réponse HTTP avec le type de contenu PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="etudiants.pdf"'

        # Générer le contenu du PDF avec ReportLab
        p = canvas.Canvas(response)
        p.drawString(100, 800, "Liste des Affectations 2024 :")

        # Positions verticales pour les lignes de texte
        y = 750
        line_height = 20
        
        # Entêtes de colonnes
        headers = [self.get_header_name(field) for field in self.list_display]
        for header_index, header in enumerate(headers):
            p.drawString(100 + header_index * 150, y, header)

        # Lignes de données pour chaque étudiant
        for etudiant in queryset:
            y -= line_height
            fields = [self.get_field_value(etudiant, field) for field in self.list_display]
            for field_index, field in enumerate(fields):
                p.drawString(100 + field_index * 150, y, field)

        p.showPage()
        p.save()

        # Retourner la réponse avec le PDF généré
        return response

    def get_header_name(self, field):
        # Traduire les noms de champ en entêtes de colonne
        if field == 'nom_etudiant':
            return "Nom"
        elif field == 'email':
            return "Email"
        elif field == 'matricule':
            return "Matricule"
        elif field == 'filiere':
            return "Filière"
        elif field == 'etablissement':
            return "Etablissement d'Affectation"

    def get_field_value(self, etudiant, field):
        # Récupérer la valeur du champ pour un étudiant donné
        if field == 'nom_etudiant':
            return etudiant.username
        elif field == 'email':
            return etudiant.email
        elif field == 'matricule':
            return etudiant.profiletudiant.matricule if etudiant.profiletudiant else ""
        elif field == 'filiere':
            return etudiant.profiletudiant.filiere.name if etudiant.profiletudiant and etudiant.profiletudiant.filiere else ""
        elif field == 'etablissement':
            return etudiant.profiletudiant.etablissement.name if etudiant.profiletudiant and etudiant.profiletudiant.etablissement else ""

    # Définir le libellé de l'action personnalisée
    export_pdf.short_description = "Exporter en PDF"

    actions = [custom_action, 'export_pdf']

    def get_list_display(self, request):
        # Récupérer la liste des champs par défaut
        list_display = list(super().get_list_display(request))
        
        # Vérifier si tous les étudiants ont un établissement non null
        if ProfilEtudiant.objects.filter(etablissement=None).exists():
            # Si oui, ajouter le champ 'etablissement' à la liste des champs à afficher
            list_display.append('etablissement')
        
        return list_display
    
    inlines = [ProfileInline]
    

    def nom_etudiant(self, obj):
        return obj.username
    
    def filiere(self, obj):
        return obj.profiletudiant.filiere
    
    def etablissement(self, obj):
        # profil = ProfilEtudiant.objects.get(user=obj)
        return obj.profiletudiant.etablissement
    etablissement.short_description = "Etablissement d'Affectation"

    def matricule(self, obj):
        # profil = ProfilEtudiant.objects.get(user=obj)
        return obj.profiletudiant.matricule
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_superuser=False)

admin.site.register(Etudiant, EtudiantAdmin)

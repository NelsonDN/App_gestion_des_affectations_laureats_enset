from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import DRegion, DDepartement, Cycle, Departement, Filiere, Etablissement, BesoinEffectif, Etudiant, ProfilEtudiant
from django.contrib.auth.models import User
from django.db.models import F
from django.utils.timezone import now

# class Etablissement_PosteForm(forms.ModelForm):

#     class Meta:
#         model = Etablissement_Poste
#         fields = ['etablissement', 'poste', 'user']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Récupérer les matières où user est null ou égal à l'utilisateur en question
#         etablissementposte = kwargs['instance']
#         etablissement = Etablissement.objects.get(pk = etablissementposte.etablissement.id)
#         poste = Poste.objects.get(pk = etablissementposte.poste.id)

#         # les departement de postes 
#         departements = Departement.objects.all()
#         employe_ids = Etablissement_Poste.objects.filter(etablissement=etablissement, poste=poste).values_list('user', flat=True)
#         all_employe_ids =  Etablissement_Poste.objects.all().values_list('user', flat=True)
#         departement_ids = ProfilEnseignant.objects.filter(user__in = employe_ids).values_list('departementOrigine', flat=True)
#         # profils = ProfilEnseignant.objects.exclude(departementOrigine__in = employe_ids).exclude(user__in = all_employe_ids)

#         # Filtrer les profils dont l'ancienneté est de anciennete_min ans ou plus
#         anciennete_min = poste.anciennete_min
#         # Calculer l'année actuelle
#         anneeCourante = now().year

#         # censeur les matieres 
#         if poste.is_censeur:
#             profil_enseignant_eligible_ids = ProfilEnseignant.objects.annotate(
#                 anciennete=anneeCourante - F('anneeSortie__year')
#             ).exclude(departementOrigine__in = employe_ids
#             ).exclude(user__in = all_employe_ids
#             ).filter(anciennete__gte=anciennete_min
#             ).filter(matiere = poste.matiere
#             ).values_list('user', flat=True)
#         else:
#             profil_enseignant_eligible_ids = ProfilEnseignant.objects.annotate(
#                 anciennete=anneeCourante - F('anneeSortie__year')
#             ).exclude(departementOrigine__in = employe_ids
#             ).exclude(user__in = all_employe_ids
#             ).filter(anciennete__gte=anciennete_min
#             ).values_list('user', flat=True)

#         users = User.objects.filter(pk__in = profil_enseignant_eligible_ids)

#         # queryset = Poste.objects.filter(user__isnull=True) | Poste.objects.filter(user=user)
#         self.fields['user'].queryset = users

class EtudiantCreationForm(forms.ModelForm):
    username = forms.CharField(label="Nom de l'étudiant")  
    email = forms.CharField(label="Email")  
    
    class Meta:
        model = Etudiant
        fields = ['username', 'email']
        


# class EnseignantEditForm(forms.ModelForm):
#     class Meta:
#         model = Enseignant
#         fields = ['username', 'email']


class ProfileEtudiantForm(forms.ModelForm):
    # filiere = forms.ModelChoiceField(queryset= Filiere.objects.all(), label="Filière")

    # rang = forms.CharField(label="Rang promotion")  
    # dateNaissance = forms.DateField(label="Date de Naissance",
    #         widget=forms.DateInput(
    #             attrs={
    #                 'class': 'form-control',
    #                 'type': 'date'
    #             }
    #         ))  
    # anneeSortie = forms.DateField(label="Année de sortie", 
    #         widget=forms.DateInput(
    #             attrs={
    #                 'class': 'form-control',
    #                 'type': 'date'
    #             }
    #         ))  
    # matricule = forms.CharField(label="Matricule")  
    # telephone = forms.CharField(label="Téléphone")  
    # sexes = [('M', 'Masculin'), ('F', "Féminin")]
    # sexe = forms.ChoiceField(label = "Catégorie", choices = sexes)

    
    
    class Meta:
        model = ProfilEtudiant
        fields = ['filiere', 'rang', 'dateNaissance', 'anneeSortie', 'matricule', 'telephone', 'sexe']

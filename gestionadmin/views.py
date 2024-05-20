from .models import DRegion, DDepartement, Cycle, Departement, Filiere, Etablissement, BesoinEffectif, Etudiant, ProfilEtudiant
from django.http import HttpResponse, HttpResponseBadRequest, FileResponse, Http404, HttpResponseForbidden
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.template import loader
from mimetypes import guess_type
from django.urls import resolve
from django.db.models import Sum, Q, F, Value
from django.db.models.functions import Coalesce

def is_not_superuser(user):
    return user.is_superuser == False


def home(request):
    user = request.user

    context = {
        "user": user,
    }
    return render(request,"gestionadmin/index.html", context)

@user_passes_test(is_not_superuser)
@login_required
def dashboard(request):
    user = request.user

    # # vérifier d'abord son rang
    user_rang = user.profiletudiant.rang
  
    try:
        # Obtenir le ProfilEtudiant du currentUser
        current_user_profile = ProfilEtudiant.objects.get(user=user)
        
        # Récupérer la filiere et le rang du currentUser
        current_filiere = current_user_profile.filiere
        current_rang = current_user_profile.rang

        # Récupérer tous les ProfilEtudiant de la même filiere avec un rang inférieur
        lower_rank_profiles = ProfilEtudiant.objects.filter(
            filiere=current_filiere,
            rang__lt=current_rang
        )

        # Vérifier si l'un des utilisateurs a un champ etablissement vide
        if lower_rank_profiles.filter(etablissement__isnull=True).exists():
            peutChoisir = False
        else:
            peutChoisir = True
    except ProfilEtudiant.DoesNotExist:
        # Si le currentUser n'a pas de ProfilEtudiant, peutchoisir est False
        return False
    
    if current_user_profile.etablissement is not None:
        peutChoisir = False
    # # recuperer les demandes par region dans son departement 
    #     #les demandes des lycees dans ce departement
    # region

    # filtrer les demandes qui ne sont pas encore atteints
    def regions_avec_un_effectif_positif(departement):
        # Annoter chaque DRegion avec la somme des nombreEffectif pour les établissements de chaque DDepartement
        regions_with_positive_effectif = DRegion.objects.annotate(
            total_effectif=Sum(
                'ddepartement__etablissement__besoineffectif__nombreEffectif',
                filter=Q(ddepartement__etablissement__besoineffectif__departement=departement)
            )
        ).filter(total_effectif__gt=0).distinct()
        
        return regions_with_positive_effectif

    regions = regions_avec_un_effectif_positif(user.profiletudiant.filiere.departement)

    def affecter_etudiant_etablissement(user, region_id):
        try:
            student_profile = user.profiletudiant
            filiere = student_profile.filiere
            besoin_effectifs = BesoinEffectif.objects.filter(
                etablissement__departement__region_id=region_id,
                departement=filiere.departement,
                nombreEffectif__gt=0
            ).select_related('etablissement').order_by('etablissement__id') 

            if besoin_effectifs.exists():
                besoin_effectif = besoin_effectifs.first()
                student_profile.etablissement = besoin_effectif.etablissement
                student_profile.save()
                besoin_effectif.nombreEffectif = F('nombreEffectif') - 1
                besoin_effectif.save()
                return True
            return False
        except ProfilEtudiant.DoesNotExist:
            return False

    if request.method == 'POST':
        choix1 = request.POST.get('choix1')
        choix2 = request.POST.get('choix2')
        choix3 = request.POST.get('choix3')
        choix4 = request.POST.get('choix4')
        choix5 = request.POST.get('choix5')
        choix6 = request.POST.get('choix6')
        choix7 = request.POST.get('choix7')
        choix8 = request.POST.get('choix8')
        choix9 = request.POST.get('choix9')
        choix10 = request.POST.get('choix10')

        choix_regions = [
            request.POST.get('choix1'),
            request.POST.get('choix2'),
            request.POST.get('choix3'),
            request.POST.get('choix4'),
            request.POST.get('choix5'),
            request.POST.get('choix6'),
            request.POST.get('choix7'),
            request.POST.get('choix8'),
            request.POST.get('choix9'),
            request.POST.get('choix10')
        ]
        
        current_user = request.user
        student_profile = current_user.profiletudiant

        # Vérifier si l'étudiant a déjà un établissement
        if student_profile.etablissement is not None:
            return redirect('gestionadmin:dashboard') 
        
        for choix in choix_regions:
            if choix and affecter_etudiant_etablissement(current_user, choix):
                return redirect('gestionadmin:dashboard')  
        return redirect('gestionadmin:dashboard')  
    
    current_url = resolve(request.path_info).url_name
    context = {
        "regions": regions,
        "user": user,
        "peutChoisir": peutChoisir,
        "current_url": current_url,
    }
    return render(request,"gestionadmin/dashboard.html", context)

@user_passes_test(is_not_superuser)
@login_required
def profile(request):
    user = request.user

    # profil_etudiant = ProfilEtudiant.objects.get(user=user)
    # # Mettre à jour le champ etablissement
    # profil_etudiant.etablissement = None
    # profil_etudiant.is_visible = False
    # # Sauvegarder les modifications
    # profil_etudiant.save()

    if request.method == 'POST':
        email = request.POST.get('email')
        user.email = email
        user.save()
        
    # a liste de toutes les DRegion avec pour chacune le total des nombreEffectif des établissements associés, filtré par un Departement donné
    regions = DRegion.objects.annotate(
        total_effectif=Coalesce(
            Sum(
                'ddepartement__etablissement__besoineffectif__nombreEffectif',
                filter=Q(ddepartement__etablissement__besoineffectif__departement=user.profiletudiant.filiere.departement)
            ),
            Value(0)
        )
    ).distinct()
    
    # Nom de la route courante
    current_url = resolve(request.path_info).url_name
    context = {
        "user": user,
        "current_url": current_url,
        "regions": regions,
    }
    return render(request,"gestionadmin/profile.html", context)

# Actions pour affecter tous les étudiants
def lancer_affectation(request):
    ProfilEtudiant.objects.all().update(is_visible=True)

    return HttpResponse("Fonction exécutée avec succès")
from django.shortcuts import render
from .models import Cours
from salle.models import Salle
from datetime import datetime

#la fonction qui renvoie la liste de toutes les salles
def cours(request):
    cours = Cours.objects.all()
    return render(request, 'cours/cours.html', {'cours': cours})

#la fonction qui renvoie la liste dessalles libres
def salles_libres(request):
    jour = request.GET.get('jour', datetime.today().strftime('%A'))  # Jour de la semaine
    heure = request.GET.get('heure', None)  # Heure de la journée (optionnel)
    
    # Filtrer les cours selon le jour et l'heure
    if heure:
        cours_occupees = Cours.objects.filter(jour=jour, heure=heure).values_list('salle_id', flat=True)
    else:
        cours_occupees = Cours.objects.filter(jour=jour).values_list('salle_id', flat=True)
    
    salles_libres = Salle.objects.exclude(id__in=cours_occupees)

    context = {
        'jour': jour,
        'heure': heure,
        'salles_libres': salles_libres
    }
    return render(request, 'cours/salles_libres.html', context)


# Fonction pour afficher les salles occupées aujourd'hui
def salles_occupees(request):
   # Récupérer le jour actuel
    jour_actuel = datetime.today().strftime('%A')

    # Filtrer les cours pour le jour actuel
    cours_aujourdhui = Cours.objects.filter(jour=jour_actuel)

    # Récupérer les salles correspondantes aux cours
    salles_occupees = [cours.salle for cours in cours_aujourdhui]

    # Contexte pour le rendu
    context = {
        'jour': jour_actuel,
        'salles_occupees': salles_occupees,
        'aucune_salle_occupee': len(salles_occupees) == 0
    }

    return render(request, 'cours/salles_occupees.html', context)
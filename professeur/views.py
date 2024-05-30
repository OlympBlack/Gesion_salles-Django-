from django.shortcuts import render
from .models import Professeur  

def professeur(request): 
    professeurs = Professeur.objects.all() 
    return render(request, 'professeur/professeur.html', {'professeurs': professeurs})

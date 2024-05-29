from django.shortcuts import render

def professeur(request):
    return render(request, 'professeur/professeur.html')
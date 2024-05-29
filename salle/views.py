from django.shortcuts import render
from .models import Salle

def index(request):
    salles = Salle.objects.all()
    return render(request, 'salle/index.html', {'salles': salles})

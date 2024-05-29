from django.shortcuts import render
from .models import Cours

# Create your views here.
def cours(request):
    cours = Cours.objects.all()
    return render(request, 'cours/cours.html', {'cours': cours})
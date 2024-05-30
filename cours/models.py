from django.db import models
from salle.models import Salle
#from professeur.models import professeur

class Cours(models.Model):
    JOURS = (
        ('Lundi', 'Lundi'),
        ('Mardi', 'Mardi'), 
        ('Mercredi', 'Mercredi'), 
        ('Jeudi', 'Jeudi'), 
        ('Vendredi', 'Vendredi')
        )
    HEURES = (
        ('07h-10h', '07h-10h'),
        ('10h-12h', '10h-12h'),
        ('15h-17h', '15h-17h'),
        ('17h-19h', '17h-18h')

    )
    libelle = models.CharField(max_length=10)
    jour = models.CharField(max_length=400, null=True, choices=JOURS)
    heure = models.CharField(max_length=400, null=True, choices=HEURES)
    salle = models.ForeignKey(Salle, null=True, on_delete=models.SET_NULL)
    #professeur = models.ForeignKey(professeur, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.libelle
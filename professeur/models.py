from django.db import models
from cours.models import Cours

class Professeur(models.Model):
    pseudo = models.CharField(max_length=20)
    telephone = models.IntegerField()
    cours = models.ForeignKey(Cours, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.pseudo

from django.db import models

class Salle(models.Model):
    numero = models.CharField(max_length=10)
    batiment = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C')])
    capacite = models.IntegerField() 

    def __str__(self):
        return f"Salle {self.numero} - {self.batiment}"

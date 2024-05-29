# salle/admin.py
from django.contrib import admin
from .models import Salle

class SalleAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero', 'batiment') 

admin.site.register(Salle, SalleAdmin)

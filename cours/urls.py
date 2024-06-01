from django.urls import path
from . import views

urlpatterns = [
     path('', views.cours, name='cours'),
     path('salles-libres/', views.salles_libres, name='salles_libres'),
     path('salles-occuoees/', views.salles_occupees, name='salles_occupees'),
]

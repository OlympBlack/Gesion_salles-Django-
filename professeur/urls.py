from django.urls import path
from . import views

urlpatterns = [
     path('', views.professeur, name='professeur'),
]

from django.db import models

# Create your models here.
class Pracownik(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    pesel = models.CharField(max_length=11, unique=True)
    stanowisko = models.CharField(max_length=50)
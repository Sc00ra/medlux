from django.db import models

# Create your models here.
class Dane(models.Model):
   Imie = models.TextField()
   Nazwisko = models.TextField()
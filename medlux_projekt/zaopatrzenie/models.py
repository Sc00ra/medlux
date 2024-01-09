from django.db import models

# Create your models here.
class zaopatrzenie(models.Model):
    nazwa = models.CharField(max_length=50)
    ilosc = models.DecimalField(max_digits=10, decimal_places=2)
    data_ostatniej_kontroli = models.CharField(max_length=11)
    miejsce_skladowania = models.CharField(max_length=50)
    wartosc_netto = models.DecimalField(max_digits=10, decimal_places=2)
    wartosc_brutto = models.DecimalField(max_digits=10, decimal_places=2)
    cena_za_szt = models.DecimalField(max_digits=10, decimal_places=2)
    opis_slowny = models.CharField(max_length=50)
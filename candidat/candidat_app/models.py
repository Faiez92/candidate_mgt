from django.core.validators import MinValueValidator
from django.db import models


class Candidat(models.Model):
    nom = models.CharField(max_length=30, blank=False, default='')
    prenom = models.CharField(max_length=30, blank=False, default='')
    email = models.EmailField(max_length=200, unique=True, blank=False, default='')
    date_naiss = models.DateField()
    tel = models.CharField(max_length=8, unique=True, blank=False, default='')
    disp = models.FloatField(range(0,6))
    exp = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    cv = models.FileField()
    msg = models.CharField(max_length=300)


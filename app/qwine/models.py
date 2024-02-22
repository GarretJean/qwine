from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django_countries.fields import CountryField


class Cepage(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"


class Vin(models.Model):
    COULEURS = {"BL": "Blanc", "RO": "Rouge", "RS": "Rosé", "OR": "Orange"}

    appelation = models.CharField(max_length=100)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    volume = models.PositiveIntegerField()
    pays = models.CharField(
        max_length=200,
        null=True,
        choices=CountryField().choices,
        db_index=True,
    )
    region = models.CharField(max_length=100, db_index=True)
    degree = models.FloatField(
        validators=[MaxValueValidator(50), MinValueValidator(0)], db_index=True
    )
    couleur = models.CharField(choices=COULEURS, default=COULEURS["RO"])
    cepages = models.ManyToManyField(Cepage)

    def __str__(self):
        return f"{self.appelation} - {self.pays} - {self.region}"

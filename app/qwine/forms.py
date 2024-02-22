from django import forms

from .models import Cave, Inventaire, Vin


class VinForm(forms.ModelForm):
    class Meta:
        model = Vin
        exclude = []


class CaveForm(forms.ModelForm):
    class Meta:
        model = Cave
        exclude = ["user"]


class InventaireForm(forms.ModelForm):
    class Meta:
        model = Inventaire
        exclude = []

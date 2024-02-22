from django import forms
from .models import Vin


class VinForm(forms.ModelForm):
    class Meta:
        model = Vin
        fields = [
            "appelation",
            "volume",
            "pays",
            "region",
            "degree",
            "couleur",
            "cepages",
        ]
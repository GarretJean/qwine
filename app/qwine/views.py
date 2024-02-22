from django.views import generic

from .models import Vin


class VinDetailView(generic.DetailView):
    model = Vin
    template_name = "detail.html"


class VinListView(generic.ListView):
    model = Vin
    template_name = "vins.html"
    context_object_name = "vins"

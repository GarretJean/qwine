from django.urls import reverse_lazy
from django.views import generic

from .models import Vin
from .forms import VinForm


class VinDetailView(generic.DetailView):
    model = Vin
    template_name = "detail.html"


class VinListView(generic.ListView):
    model = Vin
    template_name = "vins.html"
    context_object_name = "vins"


class VinCreateView(generic.CreateView):
    model = Vin
    form_class = VinForm
    template_name = "create.html"
    success_url = reverse_lazy("qwine:list")


class VinDeleteView(generic.DeleteView):
    model = Vin
    template_name = "vin_confirm_delete.html"
    success_url = reverse_lazy("qwine:list")

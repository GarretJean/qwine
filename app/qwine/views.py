from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from .forms import CaveForm, InventaireForm, VinForm
from .models import Cave, Inventaire, Vin


class SelectUserMixin:
    def get_queryset(self):
        queryset = super().get_queryset()
        # Filter the queryset to include only Vins associated with the current user
        return queryset.filter(user=self.request.user)


class VinDetailView(generic.DetailView):
    model = Vin
    template_name = "detail.html"


class VinListView(generic.ListView):
    model = Vin
    template_name = "vins.html"
    context_object_name = "vins"


class AddUserMixin:
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class VinCreateView(generic.CreateView):
    model = Vin
    form_class = VinForm
    template_name = "create.html"
    success_url = reverse_lazy("qwine:list")


class VinDeleteView(generic.DeleteView):
    model = Vin
    template_name = "vin_confirm_delete.html"
    success_url = reverse_lazy("qwine:list")


class CaveCreateView(LoginRequiredMixin, AddUserMixin, generic.CreateView):
    model = Cave
    form_class = CaveForm
    template_name = "create.html"
    success_url = reverse_lazy("qwine:cave")


class CaveListView(LoginRequiredMixin, SelectUserMixin, generic.ListView):
    model = Cave
    template_name = "caves.html"
    context_object_name = "caves"


class CaveDetailsView(generic.DetailView):
    model = Cave
    template_name = "cave_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cave = self.get_object()
        context["inventaires"] = cave.inventaire_set.all()
        return context


class InventaireCreateView(LoginRequiredMixin, AddUserMixin, generic.CreateView):
    model = Inventaire
    form_class = InventaireForm
    template_name = "create.html"

    def get_success_url(self):
        return reverse_lazy("qwine:cave")

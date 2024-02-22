from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from .forms import VinForm
from .models import Vin


class SelectUserMixin:
    def get_queryset(self):
        queryset = super().get_queryset()
        # Filter the queryset to include only Vins associated with the current user
        return queryset.filter(user=self.request.user)


class VinDetailView(LoginRequiredMixin, SelectUserMixin, generic.DetailView):
    model = Vin
    template_name = "detail.html"


class VinListView(LoginRequiredMixin, SelectUserMixin, generic.ListView):
    model = Vin
    template_name = "vins.html"
    context_object_name = "vins"


class AddUserMixin:
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class VinCreateView(LoginRequiredMixin, AddUserMixin, generic.CreateView):
    model = Vin
    form_class = VinForm
    template_name = "create.html"
    success_url = reverse_lazy("qwine:list")


class VinDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Vin
    template_name = "vin_confirm_delete.html"
    success_url = reverse_lazy("qwine:list")

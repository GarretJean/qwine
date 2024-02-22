from django.urls import path

from . import views


app_name = "qwine"

urlpatterns = [
    path("vins/<int:pk>/", views.VinDetailView.as_view(), name="detail"),
    path("", views.VinListView.as_view(), name="list"),
]

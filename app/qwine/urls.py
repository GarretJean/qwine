from django.urls import path

from . import views


app_name = "qwine"

urlpatterns = [
    path("<int:pk>/", views.VinDetailView.as_view(), name="detail"),
    path("", views.VinListView.as_view(), name="list"),
    path("create/", views.VinCreateView.as_view(), name="create"),
    path("<int:pk>/delete/", views.VinDeleteView.as_view(), name="delete"),
]

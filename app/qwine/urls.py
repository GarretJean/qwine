from django.urls import path

from . import views

app_name = "qwine"

urlpatterns = [
    path("<int:pk>/", views.VinDetailView.as_view(), name="detail"),
    path("", views.VinListView.as_view(), name="list"),
    path("create/", views.VinCreateView.as_view(), name="create"),
    path("<int:pk>/delete/", views.VinDeleteView.as_view(), name="delete"),
    path("cave/create/", views.CaveCreateView.as_view(), name="cave-create"),
    path("cave/<int:pk>/", views.CaveDetailsView.as_view(), name="cave-detail"),
    path("cave/", views.CaveListView.as_view(), name="cave"),
    path(
        "cave/<int:pk>/inventaire/create/",
        views.InventaireCreateView.as_view(),
        name="inventaire-create",
    ),
]

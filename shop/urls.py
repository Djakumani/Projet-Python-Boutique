from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("", views.accueil, name="accueil"),
    path("collection/", views.catalogue, name="catalogue"),
    path("collection/homme/", views.catalogue, {"categorie": "homme"}, name="catalogue_homme"),
    path("collection/femme/", views.catalogue, {"categorie": "femme"}, name="catalogue_femme"),
    path("collection/enfant/", views.catalogue, {"categorie": "enfant"}, name="catalogue_enfant"),
    path("acheter/<int:article_id>/", views.acheter, name="acheter"),
    path("inscription/", views.inscription, name="inscription"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("gestion/", views.gestion_articles, name="gestion_articles"),
    path("gestion/ajouter/", views.ajouter_article, name="ajouter_article"),
    path("gestion/modifier/<int:article_id>/", views.modifier_article, name="modifier_article"),
    path("gestion/supprimer/<int:article_id>/", views.supprimer_article, name="supprimer_article"),
]

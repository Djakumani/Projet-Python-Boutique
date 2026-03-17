from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "designation",
        "categorie",
        "quantite_disponible",
        "prix_unitaire",
        "date_ajout",
    )
    list_editable = ("quantite_disponible", "prix_unitaire")
    list_filter = ("categorie",)
    search_fields = ("designation", "representation")

from django.db import models


CATEGORIES = [
    ("homme", "Homme"),
    ("femme", "Femme"),
    ("enfant", "Enfant"),
]


class Article(models.Model):
    designation = models.CharField(max_length=255)
    representation = models.CharField(
        max_length=255,
        help_text="Texte descriptif ou chemin d'image dans static/img/ (ex: veste.png)",
    )
    quantite_disponible = models.PositiveIntegerField(default=0)
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    categorie = models.CharField(max_length=10, choices=CATEGORIES, default="homme")
    date_ajout = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_ajout"]

    def __str__(self):
        return f"{self.designation} ({self.get_categorie_display()})"

    @property
    def est_image(self):
        return self.representation.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp"))

    @property
    def en_stock(self):
        return self.quantite_disponible > 0

    @property
    def nom_representation(self):
        return self.representation.rsplit("/", 1)[-1]

"""
Script pour remplir la base avec des donnees de demo.
Lancer avec : python manage.py shell < init_data.py
"""

import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "boutique_vetements.settings")
django.setup()

from django.contrib.auth.models import User

from shop.models import Article


admin_user, admin_created = User.objects.get_or_create(
    username="admin",
    defaults={"email": "admin@boutique.fr", "is_staff": True, "is_superuser": True},
)
admin_user.email = "admin@boutique.fr"
admin_user.is_staff = True
admin_user.is_superuser = True
admin_user.set_password("admin123")
admin_user.save()
print("Admin disponible : admin / admin123")

client_user, client_created = User.objects.get_or_create(
    username="client1",
    defaults={"email": "client1@boutique.fr"},
)
client_user.email = "client1@boutique.fr"
client_user.set_password("client123")
client_user.save()
print("Client disponible : client1 / client123")

articles = [
    {
        "designation": "T-shirt col rond coton",
        "representation": "catalogue_assets/homme/new_collection/t_shirt_oversize_streetwear/tshirt_col_rond_coton.png",
        "quantite_disponible": 50,
        "prix_unitaire": 12.90,
        "categorie": "homme",
    },
    {
        "designation": "Chemise Oxford slim",
        "representation": "catalogue_assets/homme/hauts/chemise_slim_fit/chemise_oxford_slim.png",
        "quantite_disponible": 30,
        "prix_unitaire": 29.90,
        "categorie": "homme",
    },
    {
        "designation": "Jean selvedge regular",
        "representation": "catalogue_assets/homme/pantalons/jean_coupe_droite/jean_selvedge_regular.png",
        "quantite_disponible": 20,
        "prix_unitaire": 59.90,
        "categorie": "homme",
    },
    {
        "designation": "Robe fluide imprimee",
        "representation": "catalogue_assets/femme/robes/robe_midi_elegante/robe_fluide_imprimee.png",
        "quantite_disponible": 18,
        "prix_unitaire": 39.90,
        "categorie": "femme",
    },
    {
        "designation": "Veste legere zippee",
        "representation": "veste_cuir.png",
        "quantite_disponible": 15,
        "prix_unitaire": 49.90,
        "categorie": "femme",
    },
    {
        "designation": "Pull merinos col V",
        "representation": "pull_gris.png",
        "quantite_disponible": 0,
        "prix_unitaire": 39.90,
        "categorie": "femme",
    },
    {
        "designation": "T-shirt imprime dinosaure",
        "representation": "catalogue_assets/homme/promotion/t_shirt_graphique/tshirt_imprime_dinosaure.png",
        "quantite_disponible": 40,
        "prix_unitaire": 9.90,
        "categorie": "enfant",
    },
    {
        "designation": "Pantalon chino stretch",
        "representation": "catalogue_assets/homme/promotion/pantalon_jogger_sportif/pantalon_chino_stretch.png",
        "quantite_disponible": 25,
        "prix_unitaire": 19.90,
        "categorie": "enfant",
    },
    {
        "designation": "Robe midi elegante",
        "representation": "catalogue_assets/femme/robes/robe_midi_elegante/robe_midi_elegante.png",
        "quantite_disponible": 12,
        "prix_unitaire": 44.90,
        "categorie": "femme",
    },
    {
        "designation": "T-shirt femme oversize",
        "representation": "catalogue_assets/femme/new_collection/t_shirt_femme_oversize/tshirt_femme_oversize.png",
        "quantite_disponible": 16,
        "prix_unitaire": 24.90,
        "categorie": "femme",
    },
    {
        "designation": "Jean taille haute large",
        "representation": "catalogue_assets/femme/new_collection/jean_taille_haute_large/jean_taille_haute_large.png",
        "quantite_disponible": 10,
        "prix_unitaire": 54.90,
        "categorie": "femme",
    },
    {
        "designation": "Sac a main femme",
        "representation": "catalogue_assets/femme/accessoires/sac_a_main_femme/sac_a_main_femme.png",
        "quantite_disponible": 8,
        "prix_unitaire": 59.90,
        "categorie": "femme",
    },
    {
        "designation": "Casquette baseball",
        "representation": "catalogue_assets/homme/accessoires/casquette_baseball/casquette_baseball.png",
        "quantite_disponible": 22,
        "prix_unitaire": 14.90,
        "categorie": "homme",
    },
]

created = 0
updated = 0
for article_data in articles:
    article, was_created = Article.objects.update_or_create(
        designation=article_data["designation"],
        defaults=article_data,
    )
    if was_created:
        created += 1
        print(f"Article cree : {article.designation}")
    else:
        updated += 1
        print(f"Article mis a jour : {article.designation}")

print(f"{created} nouvel(le)(s) article(s) ajoute(s).")
print(f"{updated} article(s) mis a jour.")
print("Lancez : python manage.py runserver")
print("Acces : http://127.0.0.1:8000/")

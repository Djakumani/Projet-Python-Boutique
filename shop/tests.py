from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Article


class BoutiqueTests(TestCase):
    def setUp(self):
        self.client_user = User.objects.create_user(
            username="client1",
            password="client123",
        )
        self.staff_user = User.objects.create_user(
            username="admin_test",
            password="admin123",
            is_staff=True,
        )
        self.article_homme = Article.objects.create(
            designation="Chemise Oxford slim",
            representation="catalogue_assets/homme/hauts/chemise_slim_fit/chemise_oxford_slim.png",
            quantite_disponible=5,
            prix_unitaire="29.90",
            categorie="homme",
        )
        self.article_femme = Article.objects.create(
            designation="Robe midi elegante",
            representation="catalogue_assets/femme/robes/robe_midi_elegante/robe_fluide_imprimee.png",
            quantite_disponible=3,
            prix_unitaire="39.90",
            categorie="femme",
        )

    def test_accueil_charge(self):
        response = self.client.get(reverse("accueil"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Cozy Wardrobe")

    def test_catalogue_filtre_la_categorie(self):
        response = self.client.get(reverse("catalogue_femme"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Robe midi elegante")
        self.assertNotContains(response, "Chemise Oxford slim")

    def test_acheter_redirige_si_non_connecte(self):
        response = self.client.get(reverse("acheter", args=[self.article_homme.id]))
        self.assertEqual(response.status_code, 302)
        self.assertIn("/login/", response.url)

    def test_achat_reduit_le_stock(self):
        self.client.force_login(self.client_user)
        response = self.client.post(
            reverse("acheter", args=[self.article_homme.id]),
            {"quantite": 2},
            follow=True,
        )
        self.article_homme.refresh_from_db()
        self.assertEqual(self.article_homme.quantite_disponible, 3)
        self.assertContains(response, "Achat confirmé")

    def test_achat_refuse_stock_insuffisant(self):
        self.client.force_login(self.client_user)
        response = self.client.post(
            reverse("acheter", args=[self.article_homme.id]),
            {"quantite": 9},
            follow=True,
        )
        self.article_homme.refresh_from_db()
        self.assertEqual(self.article_homme.quantite_disponible, 5)
        self.assertContains(response, "Stock insuffisant")

    def test_inscription_cree_un_compte_et_connecte_l_utilisateur(self):
        response = self.client.post(
            reverse("inscription"),
            {
                "username": "nouveau_client",
                "email": "nouveau@example.com",
                "password1": "MotDePasseTresSolide123!",
                "password2": "MotDePasseTresSolide123!",
            },
            follow=True,
        )

        self.assertTrue(User.objects.filter(username="nouveau_client").exists())
        self.assertTrue(response.wsgi_request.user.is_authenticated)
        self.assertContains(response, "Bienvenue nouveau_client")

    def test_logout_en_post_deconnecte_l_utilisateur(self):
        self.client.force_login(self.client_user)

        response = self.client.post(reverse("logout"), follow=True)

        self.assertFalse(response.wsgi_request.user.is_authenticated)
        self.assertEqual(response.status_code, 200)

    def test_gestion_articles_reservee_au_staff(self):
        self.client.force_login(self.client_user)
        response = self.client.get(reverse("gestion_articles"))
        self.assertEqual(response.status_code, 302)

    def test_gestion_articles_accessible_au_staff(self):
        self.client.force_login(self.staff_user)
        response = self.client.get(reverse("gestion_articles"))
        self.assertEqual(response.status_code, 200)

    def test_admin_peut_ajouter_un_article(self):
        self.client.force_login(self.staff_user)

        response = self.client.post(
            reverse("ajouter_article"),
            {
                "designation": "Sac a main femme",
                "representation": "catalogue_assets/femme/accessoires/sac_a_main_femme/sac_a_main_femme.png",
                "quantite_disponible": 7,
                "prix_unitaire": "59.90",
                "categorie": "femme",
            },
            follow=True,
        )

        self.assertTrue(Article.objects.filter(designation="Sac a main femme").exists())
        self.assertContains(response, "Article ajouté.")

    def test_admin_peut_modifier_un_article(self):
        self.client.force_login(self.staff_user)

        response = self.client.post(
            reverse("modifier_article", args=[self.article_homme.id]),
            {
                "designation": self.article_homme.designation,
                "representation": self.article_homme.representation,
                "quantite_disponible": 9,
                "prix_unitaire": "34.90",
                "categorie": self.article_homme.categorie,
            },
            follow=True,
        )

        self.article_homme.refresh_from_db()
        self.assertEqual(self.article_homme.quantite_disponible, 9)
        self.assertEqual(str(self.article_homme.prix_unitaire), "34.90")
        self.assertContains(response, "modifié")

    def test_admin_peut_supprimer_un_article(self):
        self.client.force_login(self.staff_user)

        response = self.client.post(
            reverse("supprimer_article", args=[self.article_femme.id]),
            follow=True,
        )

        self.assertFalse(Article.objects.filter(id=self.article_femme.id).exists())
        self.assertContains(response, "supprimé")

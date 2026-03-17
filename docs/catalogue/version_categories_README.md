# Boutique en Ligne — Projet Django

Site de vente de vêtements en ligne développé avec Django et SQLite.
Projet universitaire "Management des Données et Innovation".


## Aperçu rapide

Pour voir le design sans rien installer, ouvre `apercu_boutique_v2.html` dans un navigateur.


## Installation

### 1. Prérequis
- Python 3.10 ou plus récent (python.org, cocher "Add to PATH")
- Git

### 2. Cloner le projet
```
git clone https://github.com/VOTRE_REPO/Projet-Python-Boutique.git
cd Projet-Python-Boutique
```

### 3. Installer Django
```
pip install django
```

### 4. Créer la base de données
```
python manage.py makemigrations shop
python manage.py migrate
```

### 5. Charger les données de démo
```
python manage.py shell < init_data.py
```

Ça crée :
- Un admin : `admin` / `admin123`
- Un client : `client1` / `client123`
- 6 articles de vêtements

### 6. Lancer le serveur
```
python manage.py runserver
```

Ouvrir http://127.0.0.1:8000/


## Fonctionnalités

### Client (utilisateur standard)
- Voir le catalogue avec les articles, prix et stock
- S'inscrire et se connecter
- Acheter des articles (le stock se met à jour automatiquement)
- Choisir la quantité à acheter

### Administrateur (is_staff=True)
- Ajouter de nouveaux articles
- Modifier les articles existants (prix, stock, description)
- Supprimer des articles
- Accès à l'interface Django admin sur /admin/


## Structure du projet

```
Projet-Python-Boutique/
├── manage.py
├── init_data.py                  ← script de données de démo
├── apercu_boutique_v2.html       ← aperçu statique du design
├── .gitignore
│
├── boutique_vetements/           ← configuration Django
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── shop/                         ← application principale
│   ├── models.py                 ← modèle Article
│   ├── views.py                  ← logique (catalogue, achat, gestion)
│   ├── forms.py                  ← formulaires
│   ├── urls.py                   ← routes
│   ├── admin.py                  ← config admin Django
│   ├── migrations/
│   └── templates/boutique/       ← pages HTML
│       ├── base.html             ← squelette (navbar, footer)
│       ├── catalogue.html        ← page d'accueil
│       ├── acheter.html          ← page d'achat
│       ├── inscription.html      ← inscription
│       └── admin/
│           ├── gestion.html      ← tableau de bord admin
│           ├── formulaire_article.html
│           └── confirmer_suppression.html
│
├── templates/registration/
│   └── login.html                ← page de connexion
│
└── static/
    ├── css/style.css             ← design (Uniqlo + Neumorphism)
    ├── js/main.js                ← animations
    └── img/                      ← images des articles (.png)
```


## Base de données

Une seule table `Article` avec ces champs :

| Champ | Type | Description |
|-------|------|-------------|
| designation | CharField(200) | Nom de l'article |
| representation | CharField(300) | Description texte ou nom d'image (.png) |
| quantite_disponible | PositiveIntegerField | Nombre en stock |
| prix_unitaire | DecimalField(10,2) | Prix en euros |
| date_ajout | DateTimeField | Date de création (automatique) |

Si le champ `representation` se termine par `.png`, le site affiche l'image depuis `static/img/`. Sinon il affiche le texte.


## Ajouter des images aux articles

1. Trouver des images libres de droits (unsplash.com, pexels.com)
2. Les renommer en `.png` et les mettre dans `static/img/`
3. Créer l'article avec le nom du fichier dans le champ representation

Exemple : image `veste.png` dans `static/img/` + article avec representation = `veste.png`


## Design

Le site utilise un style inspiré d'Uniqlo (minimaliste, épuré) combiné avec du Neumorphism (ombres douces, effet de relief).

Pas de framework CSS externe (pas de Bootstrap). Tout est dans `style.css`.

Fonctionnalités visuelles :
- Carrousel hero vertical avec 3 slides (défilement auto + swipe mobile)
- Zoom image au survol des cartes produits
- Apparition progressive des éléments au scroll
- Animation de confirmation sur le bouton d'achat
- Effet ripple sur les boutons
- Alertes qui disparaissent automatiquement


## Répartition du travail

| Rôle | Tâches |
|------|--------|
| Modèle / BDD | models.py, init_data.py, migrations |
| Backend admin | views.py (partie gestion), forms.py (ArticleForm) |
| Backend client | views.py (catalogue, achat), forms.py (AchatForm) |
| Frontend | Templates HTML, CSS, JS, images |
| Config / Doc | settings.py, urls.py, README, rapport |


## Technologies

- Python 3 + Django 6
- SQLite
- HTML / CSS / JavaScript (vanilla, aucune librairie)

# Guide Frontend — Pour bosser sur le HTML/CSS/JS

## C'est quoi ce projet ?

Un site de vente de vêtements en ligne fait avec Django (Python). Toi t'as pas besoin de toucher au Python, juste au HTML, CSS et JS.

Le design est inspiré d'Uniqlo avec un style Neumorphism (ombres douces, effet de relief sur les boutons et les cartes).


## Où sont les fichiers qui te concernent ?

```
static/
├── css/style.css          ← TOUT le design est là
├── js/main.js             ← les animations (carrousel, zoom, scroll)
└── img/                   ← les images des articles (.png)

shop/templates/boutique/
├── base.html              ← le squelette commun (navbar + footer)
├── catalogue.html         ← page d'accueil avec grille produits
├── acheter.html           ← page quand on clique sur un article
├── inscription.html       ← formulaire d'inscription
└── admin/
    ├── gestion.html       ← tableau de bord admin
    ├── formulaire_article.html  ← formulaire ajout/modif
    └── confirmer_suppression.html

templates/registration/
└── login.html             ← page de connexion
```

Tu touches UNIQUEMENT à ces fichiers. Le reste c'est du Python, t'y touches pas.


## Comment voir le site sans installer Python ?

Ouvre le fichier `apercu_boutique_v2.html` dans ton navigateur (double-clic). C'est une version statique avec des données en dur, ça te montre le rendu complet avec les animations.


## Comment voir le vrai site (avec Django) ?

Si t'as envie de tester tes modifs en live :

1. Installe Python depuis python.org (coche "Add to PATH")
2. Dans le terminal :
```
pip install django
python manage.py makemigrations shop
python manage.py migrate
python manage.py shell < init_data.py
python manage.py runserver
```
3. Ouvre http://127.0.0.1:8000/

Comptes de test : admin / admin123 et client1 / client123


## Comment marche le HTML dans Django ?

Les fichiers HTML sont des "templates". C'est du HTML normal MAIS avec des balises spéciales :

`{{ variable }}` → affiche une donnée de la base. Par exemple `{{ article.prix_unitaire }}` sera remplacé par "29.90" quand Django charge la page.

`{% if condition %}` → condition. Genre `{% if article.en_stock %}` affiche le bouton acheter seulement si y'a du stock.

`{% for article in articles %}` → boucle. Crée une carte pour chaque article dans la base.

`{% extends "boutique/base.html" %}` → dit que cette page utilise le squelette de base.html (navbar, footer, CSS, JS).

`{% block content %}` → c'est la zone qui change d'une page à l'autre. Le reste (navbar, footer) vient de base.html.

`{% static 'css/style.css' %}` → chemin vers un fichier dans le dossier static/

`{% url 'catalogue' %}` → génère le lien vers une page. Pas besoin de taper l'URL en dur.

En gros : tu peux modifier tout le HTML et le CSS normalement, faut juste pas supprimer les trucs entre `{{ }}` et `{% %}`.


## Le CSS — comment c'est organisé

Le fichier `style.css` fait environ 500 lignes. Voilà les sections dans l'ordre :

- Reset et body
- Animations (apparition au scroll)
- Navbar
- Alertes / messages
- Carrousel hero (la bannière qui défile)
- Grille produits
- Carte produit (avec le zoom au hover)
- Boutons (primary, red, outline, disabled)
- Effets (ripple au clic, spinner)
- Page d'achat
- Formulaires (connexion, inscription, ajout article)
- Tableau admin
- Page de confirmation suppression
- Footer

Les couleurs principales :
- Fond : `#E0E4E7`
- Ombres claires : `#ffffff`
- Ombres foncées : `#b8c7dd`
- Texte : `#111111`
- Texte secondaire : `#646464`
- Rouge (bouton acheter) : `#C0392B`
- Vert (en stock) : `#2D7D2D`

L'effet neumorphism c'est toujours le même principe :
```css
/* relief (sort de la surface) */
box-shadow: 6px 6px 14px #b8c7dd, -6px -6px 14px #ffffff;

/* creux (enfoncé dans la surface) */
box-shadow: inset 4px 3px 3px 0px #b8c7dd, inset -2px -4px 4px 0px #fff;
```


## Le JS — les 4 fonctionnalités

`main.js` fait environ 120 lignes. Voilà ce qu'il fait :

1. **Carrousel hero** — les 3 slides défilent toutes les 4 secondes, on peut cliquer sur les points ou swiper sur mobile
2. **Zoom image** — quand tu survoles une carte produit, l'image grossit et un overlay "VOIR LE PRODUIT" apparait
3. **Apparition au scroll** — les cartes apparaissent en glissant vers le haut quand on scrolle
4. **Animation d'achat** — le bouton "Acheter" affiche un spinner au clic. Les boutons "Ajouter au panier" ont un effet ripple


## Comment ajouter une image pour un article ?

1. Trouve une image libre de droits (unsplash.com, pexels.com)
2. Renomme-la en .png (ex: `chemise.png`)
3. Mets-la dans `static/img/`
4. Dans la base de données, le champ "representation" de l'article doit contenir exactement le meme nom (ex: `chemise.png`)

Le template affichera automatiquement l'image au lieu du texte.

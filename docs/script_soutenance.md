# Script de soutenance

## Duree conseillee

- 8 a 10 minutes de presentation
- 2 a 4 minutes de demonstration
- 2 a 5 minutes de questions

## Repartition de la parole

- Zeinabou : introduction, structure du projet, conclusion
- Assia : base de donnees, modele Article, partie admin
- Awa : logique metier, achat, mise a jour du stock
- Alexis : design, experience utilisateur, interface
- Chloe : tests, documentation, difficultes rencontrees

## Slide 1 - Titre

### Qui parle

- Zeinabou

### Ce que tu peux dire

"Bonjour, nous allons vous presenter notre projet de boutique en ligne realise avec Django dans le cadre du cours Management des donnees et innovation. Le projet distingue deux types d'utilisateurs : les clients et les administrateurs."

## Slide 2 - Plan de presentation

### Qui parle

- Zeinabou

### Ce que tu peux dire

"Nous allons d'abord rappeler l'objectif du projet, puis expliquer le fonctionnement du site, la structure du code, la repartition du travail dans le groupe, les choix de design, ensuite nous ferons une demonstration, puis nous terminerons par les difficultes rencontrees et la conclusion."

## Slide 3 - Objectif et fonctionnement general

### Qui parle

- Zeinabou

### Ce que tu peux dire

"L'objectif etait de developper un site de vente en ligne avec Django et SQLite. Le client peut consulter les articles, voir l'image, le stock et le prix, puis acheter une quantite disponible. L'administrateur peut ajouter, modifier et supprimer des articles."

## Slide 4 - Ce que le site permet de faire

### Qui parle

- Awa

### Ce que tu peux dire

"Cote client, on a la connexion, l'inscription, le catalogue par categories et l'achat. Cote administrateur, on a une interface de gestion qui permet de modifier le contenu de la boutique. Lorsqu'un client achete un article, la quantite disponible diminue automatiquement."

## Slide 5 - Structure du code

### Qui parle

- Zeinabou puis Assia

### Ce que vous pouvez dire

Zeinabou :
"Le projet est compose d'un projet Django principal et d'une application principale."

Assia :
"Les fichiers principaux sont :"

- `boutique_vetements/settings.py` : configuration generale du projet
- `shop/models.py` : definition du modele `Article`
- `shop/views.py` : logique des pages et actions
- `shop/forms.py` : formulaires d'achat, d'inscription et d'administration
- `shop/urls.py` : routage des pages
- `templates/` : toutes les pages HTML
- `static/` : images, CSS et JavaScript
- `init_data.py` : creation des comptes et des donnees de demonstration
- `shop/tests.py` : verification automatique des parcours importants

## Slide 6 - Base de donnees et role admin

### Qui parle

- Assia

### Ce que tu peux dire

"Dans la base SQLite, chaque article contient une designation, une representation, une quantite disponible, un prix unitaire et une categorie. L'administrateur peut ajouter un article, modifier son image, son prix ou son stock, et supprimer un article si besoin."

## Slide 7 - Logique metier

### Qui parle

- Awa

### Ce que tu peux dire

"La logique metier est geree dans les vues Django. Quand un client clique sur acheter, le formulaire verifie la quantite demandee. Si la quantite est disponible, le stock est mis a jour. Sinon, un message d'erreur s'affiche. On a aussi protege certaines pages pour qu'elles soient reservees aux administrateurs."

## Slide 8 - Choix de design

### Qui parle

- Alexis

### Ce que tu peux dire

"Pour le design, on a choisi une interface e-commerce simple, lisible et moderne. On a privilegie une grille de produits claire, des cartes visuelles, un menu simple et une palette sobre. Le but etait d'avoir un rendu propre sans perdre du temps sur un design trop complexe, parce que la priorite du projet restait la fonctionnalite."

### Pourquoi ce choix

- lecture rapide pour le professeur
- navigation simple entre accueil, catalogue, login et gestion
- mise en avant du prix, du stock et de l'image
- design coherent avec une boutique de vetements

## Slide 9 - Repartition du travail

### Qui parle

- Chloe

### Ce que tu peux dire

"Nous nous sommes repartis le travail par roles."

- Zeinabou : structure du projet, URLs, integration finale et verification
- Assia : modele Article, base de donnees, categories, administration
- Awa : logique d'achat, stock, vues backend
- Alexis : templates HTML, CSS, JavaScript, interface visuelle
- Chloe : donnees de demonstration, tests, captures et documentation

## Slide 10 - Demonstration

### Qui parle

- Alexis pour lancer
- Awa pour expliquer le parcours client
- Assia pour le parcours admin

### Ce que vous pouvez dire

"Nous allons maintenant vous montrer le fonctionnement du site."

### Deroule conseille

1. Ouvrir la page d'accueil
2. Aller sur le catalogue
3. Montrer les categories homme, femme, enfant
4. Se connecter en client avec `client1 / client123`
5. Ouvrir un article et acheter une quantite
6. Montrer le message de confirmation
7. Revenir au catalogue et verifier que le stock a baisse
8. Se connecter en admin avec `admin / admin123`
9. Ouvrir la gestion
10. Montrer qu'on peut ajouter, modifier ou supprimer un article

### Phrase utile pendant la demo

"Quand on effectue cette action, la base de donnees est mise a jour et le changement est visible tout de suite dans l'interface."

## Slide 11 - Difficultes rencontrees

### Qui parle

- Chloe

### Ce que tu peux dire

"Nous avons rencontre plusieurs difficultes."

- integration de contributions venant de plusieurs personnes
- certains membres ne maitrisaient pas encore bien GitHub
- besoin de renommer et ranger correctement les images
- adaptation de maquettes HTML/CSS dans une vraie structure Django
- verification de la logique de stock pour eviter des erreurs lors des achats

### Comment vous pouvez presenter les solutions

- centralisation et integration finale par Zeinabou
- tests des parcours importants
- nettoyage des noms d'images et des chemins dans la base
- ajout de donnees de demonstration et de captures d'ecran

## Slide 12 - Conclusion

### Qui parle

- Zeinabou

### Ce que tu peux dire

"Pour conclure, notre projet repond au cahier des charges : il distingue bien les roles client et administrateur, il permet la consultation et l'achat d'articles, ainsi que la gestion du stock et des produits. Nous avons egalement prepare une demonstration complete, des tests et une documentation de rendu."

## Questions probables du prof

### Pourquoi avoir choisi Django ?

"Parce que Django permet de structurer rapidement un projet web complet avec base de donnees, administration, formulaires et gestion des utilisateurs."

### Pourquoi SQLite ?

"Parce que c'etait suffisant pour un projet de cours, simple a integrer et conforme au cahier des charges."

### Comment le stock est-il mis a jour ?

"Lors d'un achat, la quantite demandee est verifiee, puis la quantite disponible est decrementee dans la base de donnees."

### Pourquoi ce design ?

"Nous avons privilegie un design clair et lisible, adapte a une boutique de vetements, avec la priorite donnee a la comprehension et a la demonstration des fonctionnalites."

## Note importante

Pour la demo, ouvrez le site avant la presentation avec :

```powershell
python init_data.py
python manage.py runserver
```

Puis preparez a l'avance :

- l'onglet accueil
- l'onglet catalogue
- l'onglet login
- l'onglet gestion admin

# Projet Python Boutique

Boutique en ligne realisee avec Django et SQLite pour le cours "Management des donnees et innovation".

## Lancer le projet

1. Creer un environnement virtuel :
   `python -m venv venv`
2. Activer l'environnement :
   `venv\\Scripts\\activate`
3. Installer les dependances :
   `pip install -r requirements.txt`
4. Installer Chromium pour les captures et le PDF (optionnel) :
   `python -m playwright install chromium`
5. Appliquer les migrations :
   `python manage.py migrate`
6. Charger les comptes et les articles de demonstration :
   `python init_data.py`
7. Lancer le serveur :
   `python manage.py runserver`

Acces local : `http://127.0.0.1:8000/`

## Comptes de demonstration

- Admin : `admin / admin123`
- Client : `client1 / client123`

## Commandes utiles

- Verifier le projet : `python manage.py check`
- Lancer les tests : `python manage.py test`
- Regenerer les captures : `python scripts/capture_demo_screenshots.py`
- Regenerer la presentation PowerPoint : `python scripts/generate_presentation.py`

## Structure utile

- Application Django : `shop/`
- Templates : `templates/`
- Assets statiques : `static/`
- Rapport et captures : `docs/`

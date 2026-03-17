from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AchatForm, ArticleForm, InscriptionForm
from .models import Article, CATEGORIES


def accueil(request):
    articles = Article.objects.all()[:6]
    return render(request, "boutique/accueil.html", {"articles": articles})


def catalogue(request, categorie=None):
    if categorie:
        articles = Article.objects.filter(categorie=categorie)
        titre = dict(CATEGORIES).get(categorie, "Collection")
    else:
        articles = Article.objects.all()
        titre = "Toute la collection"

    return render(
        request,
        "boutique/catalogue.html",
        {
            "articles": articles,
            "titre": titre,
            "categorie_active": categorie,
            "categories": CATEGORIES,
        },
    )


def inscription(request):
    if request.method == "POST":
        form = InscriptionForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Bienvenue {user.username} !")
            return redirect("accueil")
    else:
        form = InscriptionForm()

    return render(request, "boutique/inscription.html", {"form": form})


@login_required
def acheter(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.method == "POST":
        form = AchatForm(request.POST)
        if form.is_valid():
            quantite = form.cleaned_data["quantite"]
            updated = Article.objects.filter(
                id=article.id,
                quantite_disponible__gte=quantite,
            ).update(quantite_disponible=F("quantite_disponible") - quantite)

            if not updated:
                article.refresh_from_db()
                messages.error(
                    request,
                    f"Stock insuffisant ({article.quantite_disponible} disponible(s)).",
                )
            else:
                article.refresh_from_db()
                total = quantite * article.prix_unitaire
                messages.success(
                    request,
                    f"Achat confirmé : {quantite} x {article.designation} - {total:.2f} €",
                )
                return redirect("catalogue")
    else:
        form = AchatForm()

    return render(request, "boutique/acheter.html", {"article": article, "form": form})


@staff_member_required
def gestion_articles(request):
    articles = Article.objects.all()
    return render(request, "boutique/admin/gestion.html", {"articles": articles})


@staff_member_required
def ajouter_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Article ajouté.")
            return redirect("gestion_articles")
    else:
        form = ArticleForm()

    return render(
        request,
        "boutique/admin/formulaire_article.html",
        {"form": form, "titre": "Ajouter un article"},
    )


@staff_member_required
def modifier_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, f"Article '{article.designation}' modifié.")
            return redirect("gestion_articles")
    else:
        form = ArticleForm(instance=article)

    return render(
        request,
        "boutique/admin/formulaire_article.html",
        {"form": form, "titre": f"Modifier : {article.designation}"},
    )


@staff_member_required
def supprimer_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == "POST":
        nom = article.designation
        article.delete()
        messages.success(request, f"Article '{nom}' supprimé.")
        return redirect("gestion_articles")

    return render(
        request,
        "boutique/admin/confirmer_suppression.html",
        {"article": article},
    )

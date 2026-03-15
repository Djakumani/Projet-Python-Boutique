from django.shortcuts import render, get_object_or_404, redirect
from .models import Article

def catalogue(request):
    articles = Article.objects.all()
    return render(request, 'boutique/catalogue.html', {'articles': articles})

def acheter(request, article_id):
    if request.method == 'POST':
        article = get_object_or_404(Article, id=article_id)
        if article.quantite_disponible > 0:
            article.quantite_disponible -= 1
            article.save()
    return redirect('catalogue')

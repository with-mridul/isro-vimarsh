from django.shortcuts import render, get_object_or_404
from .models import NewsArticle

def news_list(request):
    news_articles = NewsArticle.objects.filter(is_published=True)
    context = {
        'news_articles': news_articles,
    }
    return render(request, 'news/news_list.html', context)

def news_detail(request, slug):
    article = get_object_or_404(NewsArticle, slug=slug, is_published=True)
    context = {
        'article': article,
    }
    return render(request, 'news/news_detail.html', context)
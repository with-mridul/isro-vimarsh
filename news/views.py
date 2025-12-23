from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import NewsArticle, Category

def news_list(request):
    # Get category filter from URL parameter
    selected_category = request.GET.get('category', None)
    
    # Filter news articles
    if selected_category:
        news_articles = NewsArticle.objects.filter(
            is_published=True,
            category__slug=selected_category
        )
    else:
        news_articles = NewsArticle.objects.filter(is_published=True)
    
    # Get featured article (first one marked as featured)
    featured_article = news_articles.filter(is_featured=True).first()
    
    # Pagination - 9 articles per page (or 8 if featured exists)
    articles_per_page = 8 if featured_article else 9
    paginator = Paginator(news_articles, articles_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get all categories for filter
    categories = Category.objects.all()
    
    context = {
        'news_articles': page_obj,
        'featured_article': featured_article,
        'categories': categories,
        'selected_category': selected_category,
        'is_paginated': page_obj.has_other_pages(),
        'page_obj': page_obj,
    }
    return render(request, 'news/news_list.html', context)

def news_detail(request, slug):
    article = get_object_or_404(NewsArticle, slug=slug, is_published=True)
    
    # Get related articles (same category, exclude current)
    related_articles = NewsArticle.objects.filter(
        category=article.category,
        is_published=True
    ).exclude(id=article.id)[:3]
    
    context = {
        'article': article,
        'related_articles': related_articles,
    }
    return render(request, 'news/news_detail.html', context)
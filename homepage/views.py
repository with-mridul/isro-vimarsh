from django.shortcuts import render
from missions.models import Mission
from news.models import NewsArticle
from .models import ISROAchievement

def home(request):
    featured_missions = Mission.objects.filter(featured_on_homepage=True).order_by('homepage_order')[:3]
    latest_news = NewsArticle.objects.filter(is_published=True)[:3]
    
    context = {
        'featured_missions': featured_missions,
        'latest_news': latest_news,
    }
    return render(request, 'homepage/home.html', context)

def history(request):
    achievements = ISROAchievement.objects.all().order_by('year')
    context = {
        'achievements': achievements,
    }
    return render(request, 'homepage/history.html', context)

def about(request):
    return render(request, 'homepage/about.html')
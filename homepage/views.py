from django.shortcuts import render
from missions.models import Mission
from news.models import NewsArticle
from rockets.models import Rocket
from .models import IsroAchievement

def home(request):
    featured_missions = Mission.objects.filter(featured_on_homepage=True).order_by('homepage_order')[:6]
    latest_news = NewsArticle.objects.filter(is_published=True)[:3]
    
    # Stats for quick glance section
    total_missions = Mission.objects.count()
    total_rockets = Rocket.objects.count()
    total_achievements = IsroAchievement.objects.count()
    
    context = {
        'featured_missions': featured_missions,
        'latest_news': latest_news,
        'total_missions': total_missions,
        'total_rockets': total_rockets,
        'total_achievements': total_achievements,
    }
    return render(request, 'homepage/home.html', context)

def history(request):
    achievements = IsroAchievement.objects.all().order_by('year')
    context = {
        'achievements': achievements,
    }
    return render(request, 'homepage/history.html', context)

def about(request):
    return render(request, 'homepage/about.html')
from django.contrib import admin
from .models import IsroAchievement, SiteSettings

@admin.register(IsroAchievement)
class IsroAchievementAdmin(admin.ModelAdmin):
    list_display = ['year', 'title', 'category']
    list_filter = ['year', 'category']
    search_fields = ['title', 'description']

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['site_name', 'tagline']
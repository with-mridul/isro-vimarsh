from django.contrib import admin
from .models import Mission

@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'mission_type', 'status', 'launch_date', 'featured_on_homepage']
    list_filter = ['mission_type', 'status', 'featured_on_homepage']
    search_fields = ['name', 'full_name', 'description']
    list_editable = ['featured_on_homepage']
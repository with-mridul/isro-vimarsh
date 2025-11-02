from django.contrib import admin
from .models import Rocket

# Register your models here.
@admin.register(Rocket)
class RocketAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'total_launches', 'success_rate']
    list_filter = ['status', 'first_launch']
    search_fields = ['name', 'full_name', 'description']
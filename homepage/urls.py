from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.home, name='home'),
    path('history/', views.history, name='history'),
    path('about/', views.about, name='about'),
]
from django.urls import path
from . import views

app_name = 'rockets'

urlpatterns = [
    path('', views.rocket_list, name='rocket_list'),
    path('<int:pk>/', views.rocket_detail, name='rocket_detail'),
]
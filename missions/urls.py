from django.urls import path
from . import views

app_name = 'missions'

urlpatterns = [
    path('', views.mission_list, name='mission_list'),
    path('<int:pk>/', views.mission_detail, name='mission_detail'),
]
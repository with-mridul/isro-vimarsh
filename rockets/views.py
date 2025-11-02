from django.shortcuts import render, get_object_or_404
from .models import Rocket

def rocket_list(request):
    rockets = Rocket.objects.all()
    context = {
        'rockets': rockets,
    }
    return render(request, 'rockets/rocket_list.html', context)

def rocket_detail(request, pk):
    rocket = get_object_or_404(Rocket, pk=pk)
    context = {
        'rocket': rocket,
    }
    return render(request, 'rockets/rocket_detail.html', context)
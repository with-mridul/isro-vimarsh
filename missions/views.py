from django.shortcuts import render, get_object_or_404
from .models import Mission

def mission_list(request):
    # Get filter from URL parameter
    mission_type = request.GET.get('type', None)
    status = request.GET.get('status', None)
    
    missions = Mission.objects.all()
    
    # Apply filters
    if mission_type:
        missions = missions.filter(mission_type=mission_type)
    if status:
        missions = missions.filter(status=status)
    
    # Get all unique mission types that exist in database
    existing_types = Mission.objects.values_list('mission_type', flat=True).distinct()
    mission_types = []
    for choice_value, choice_label in Mission.MISSION_TYPE_CHOICES:
        if choice_value in existing_types:
            mission_types.append({'value': choice_value, 'label': choice_label})
    
    # Get all unique statuses that exist in database
    existing_statuses = Mission.objects.values_list('status', flat=True).distinct()
    statuses = []
    for choice_value, choice_label in Mission.STATUS_CHOICES:
        if choice_value in existing_statuses:
            statuses.append({'value': choice_value, 'label': choice_label})
    
    context = {
        'missions': missions,
        'mission_types': mission_types,
        'statuses': statuses,
        'selected_type': mission_type,
        'selected_status': status,
    }
    return render(request, 'missions/mission_list.html', context)

def mission_detail(request, pk):
    mission = get_object_or_404(Mission, pk=pk)
    
    # Get related missions (same type, exclude current)
    related_missions = Mission.objects.filter(
        mission_type=mission.mission_type
    ).exclude(id=mission.id)[:3]
    
    context = {
        'mission': mission,
        'related_missions': related_missions,
    }
    return render(request, 'missions/mission_detail.html', context)
from datetime import timedelta, timezone

from django.shortcuts import render
from django.utils.timezone import localtime

from datacenter.models import Visit

TZ_MSK = timezone(timedelta(hours=3))
     

def get_duration(visit):
    if visit.leaved_at:
        return visit.leaved_at - visit.entered_at
    else:
        return (localtime(timezone=TZ_MSK).replace(microsecond=0) - 
                localtime(visit.entered_at, timezone=TZ_MSK))
    

def format_duration(duration):
    duration = int(duration.total_seconds())
    hours = duration // 3600
    minutes = (duration - hours * 3600) // 60
    if hours < 24:
        return f'{hours}:{minutes}:00'
    else:
        return f'{hours // 24}::{hours % 24}:{minutes}:00'


def storage_information_view(request):
    still_there = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []

    for person in still_there:
        non_closed_visits.append({
            'who_entered': person.passcard.owner_name,
            'entered_at': localtime(person.entered_at, timezone=TZ_MSK),
            'duration': format_duration(get_duration(person)),
        })
    
    context = {
        'non_closed_visits': non_closed_visits,
    }

    return render(request, 'storage_information.html', context)

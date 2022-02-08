from datetime import timedelta, timezone

from django.shortcuts import render

from datacenter.models import Passcard, Visit
from datacenter.storage_information_view import format_duration, get_duration

TZ_MSK = timezone(timedelta(hours=3))


def passcard_info_view(request, passcode, alarm_time = 3600):
    selected_passcard = Passcard.objects.get(passcode=passcode)

    selected_passcard_visits = []

    for visit in Visit.objects.filter(passcard=selected_passcard):
        entered_at = visit.entered_at

        if visit.leaved_at:
            how_long_inside = visit.leaved_at - entered_at
        else:
            how_long_inside = get_duration(visit)
        
        is_strange = how_long_inside.total_seconds() >= alarm_time
        
        selected_passcard_visits.append(
            {
                'entered_at': entered_at,
                'duration': format_duration(how_long_inside),
                'is_strange': is_strange
            }
        )
    
    context = {
        'passcard': selected_passcard,
        'this_passcard_visits': selected_passcard_visits
    }

    return render(request, 'passcard_info.html', context)

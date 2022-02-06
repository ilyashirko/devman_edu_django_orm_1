from datetime import timedelta, timezone

from django.shortcuts import render

from datacenter.models import Passcard, Visit
from datacenter.storage_information_view import format_duration, get_duration

TZ_MSK = timezone(timedelta(hours=3))

def passcard_info_view(request, passcode, alarm_time = 3600):
    passcard = Passcard.objects.get(passcode=passcode)

    this_passcard_visits = []
    for visit in Visit.objects.filter(passcard=passcard):
        entered_at = visit.entered_at
        try:
            how_long_inside = visit.leaved_at - entered_at
        except TypeError:
            how_long_inside = get_duration(visit)
        finally:
            is_strange = False
            if how_long_inside.total_seconds() >= alarm_time:
                is_strange = True
            
            this_passcard_visits.append(
                {
                    'entered_at': entered_at,
                    'duration': format_duration(how_long_inside),
                    'is_strange': is_strange
                }
            )

    
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)

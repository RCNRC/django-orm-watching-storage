from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import get_duration, format_duration, is_visit_long
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    this_passcard_visits = []
    visits = Visit.objects.filter(passcard=passcard)
    for visit in visits:
        this_passcard_visits.append({
            "entered_at": f"{visit.entered_at}",
             "duration": f"{format_duration(get_duration(visit=visit))}",
             "is_strange": f"{is_visit_long(visit)}",
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)

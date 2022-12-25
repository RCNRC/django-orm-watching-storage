from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import get_duration, format_duration
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits = []
    visits = Visit.objects.filter(leaved_at__isnull=True)
    for visit in visits:
        non_closed_visits.append({
            "who_entered": f"{visit.passcard.owner_name}",
            "entered_at": f"{visit.entered_at}",
            "duration": f"{format_duration(get_duration(visit=visit))}",
        })

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)

from django.db import models
from django.utils.timezone import localtime


def get_duration(visit):
    return localtime(visit.leaved_at) - localtime(visit.entered_at)


def format_duration(duration):
    duration_hours = int(duration.total_seconds()//3600)
    duration_minutes = int(duration.total_seconds()//60%60)
    if duration.total_seconds() <= 86399:
        return f"{duration_hours}ч {duration_minutes}м"
    else:
        duration_days = int(duration.total_seconds()//(24*3600))
        return f"{duration_days}д {duration_hours}ч {duration_minutes}м"


def is_visit_long(visit, minutes=60):
    return True if get_duration(visit=visit).seconds//60 > minutes else False


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

import django_filters

from workshops.models import Event

class EventFilter(django_filters.FilterSet):
    class Meta:
        model = Event
        fields = ['event_type']
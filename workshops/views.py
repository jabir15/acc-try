from django.utils import timezone
from django.views.generic import ListView

from workshops.models import Event

# Create your views here.
class EventListView(ListView):

    model = Event
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
    
    def get_queryset(self):
        return Event.objects.all().order_by("-enddate")[:10]
        # return Event.objects.all().filter(type='SR').order_by("-enddate")[:10]
    

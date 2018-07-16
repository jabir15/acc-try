from django.views.generic import ListView

from workshops.models import Event

# Create your views here.


class EventListView(ListView):

    model = Event

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        option = self.request.GET.get('option', 'AE')
        if option == 'WS':
            context['event_list'] = Event.objects.filter(event_type=option).order_by('-created_at')
            return context
        elif option == 'SR':
            context['event_list'] = Event.objects.filter(event_type=option).order_by('-created_at')
            return context
        else:
            context['event_list'] = Event.objects.all().order_by('-created_at')
            return context

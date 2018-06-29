from django.utils import timezone
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from django.shortcuts import render

from workshops.models import Event

# Create your views here.
class EventListView(ListView):

    model = Event
    paginate_by = 10

@csrf_protect
def post(request):
    events = Event.objects.all().order_by("-enddate")[:10]
    return render(request, 'workshops/event_list.html', { 'event_list': events })

def ajax(self, request):
    response_dict = {
        'success': True
    }
    action = request.POST.get('action', '')
    if action=='select_event':
        option = request.POST.get('option','')
    if hasattr(self, action):
        response_dict = getattr(self, action)(request)
        if option == "Workshops":
            response_dict = {
                'events': Event.objects.all().filter(event_type='WS').order_by("-enddate")
            }
        elif option == "Seminars":
            response_dict = {
                'events': Event.objects.all().filter(event_type='SR').order_by("-enddate")
            }
        else:
            response_dict = {
                'events': Event.objects.all().order_by("-enddate")[:10]
            }
    return JsonResponse(response_dict)

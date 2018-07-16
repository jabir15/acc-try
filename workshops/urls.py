from django.urls import path
from workshops.views import EventListView


urlpatterns = [
    path('', EventListView.as_view() , name='event-list'),
]
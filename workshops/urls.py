from django.urls import path
from workshops.views import EventListView

from . import views

urlpatterns = [
    path('', EventListView.as_view() , name='event-list'),
]
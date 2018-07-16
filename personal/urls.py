from django.urls import path,include
from . import views
from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='/static/personal/img/favicon.ico', permanent=True)

urlpatterns = [
    path('favicon.ico/', favicon_view, name='favicon'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('listofcolleges/', views.colleges ,name='list-of-colleges'),
    path('',views.index, name='index'),
]
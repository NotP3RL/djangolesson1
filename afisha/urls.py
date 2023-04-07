from django.urls import path
from .views import show_index, get_place_payload

appname='afisha'
urlpatterns = [
    path('', show_index, name='index'),
    path('places/<id>', get_place_payload, name='index')
]
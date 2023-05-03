from django.urls import include, path
from .views import show_index, get_place_payload

appname = 'afisha'
urlpatterns = [
    path('', show_index, name='index'),
    path('places/<place_id>', get_place_payload, name='place_payload'),
    path('tinymce/', include('tinymce.urls')),
]

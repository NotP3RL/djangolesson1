from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Place


def show_index(request):
    places = Place.objects.all()
    context = {
        'places': {
            'type': 'FeatureCollection',
            'features': [
                {
                    'type': 'Feature',
                    'geometry': {
                        'type': 'Point',
                        'coordinates': [place.lng, place.lat]
                    },
                    'properties': {
                        'title': place.title,
                        'placeId': place.id,
                        'detailsUrl': reverse('place_payload', kwargs={'place_id': place.id})
                    }
                } for place in places
            ]
        }
    }
    return render(request, 'index.html', context=context)


def get_place_payload(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_payload = {
        'title': place.title,
        'imgs': [image.image.url for image in place.images.all()],
        'description_short': place.short_description,
        'description_long': place.long_description,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat
        }
    }
    return JsonResponse(place_payload, json_dumps_params={'ensure_ascii': False})

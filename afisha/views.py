from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from django.urls import reverse

from .models import Place


def show_index(request):
    template = loader.get_template('index.html')
    places = Place.objects.all()
    context = {
        "places": {"type": "FeatureCollection",
                   "features": [
                       {
                           "type": "Feature",
                           "geometry": {
                               "type": "Point",
                               "coordinates": [place.lng, place.lat]
                           },
                           "properties": {
                               "title": place.title,
                               "placeId": place.id,
                               "detailsUrl": reverse('place_payload', kwargs={'place_id': place.id})
                           }
                       } for place in places
                   ]}
    }
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)


def get_place_payload(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_payload = {
        "title": place.title,
        "imgs": [image.image.url for image in place.images.all()],
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat
        }
    }
    return JsonResponse(place_payload, json_dumps_params={'ensure_ascii': False})

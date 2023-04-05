from django.http import HttpResponse
from django.template import loader
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
                               "detailsUrl": "./static/places/moscow_legends.json"
                           }
                       } for place in places
                   ]}
    }
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)

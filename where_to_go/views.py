from django.http import HttpResponse
from django.shortcuts import render

from places.models import Place


def index(request):
    """Вью главной страницы."""

    places_geojson = {"type": "FeatureCollection", "features": []}

    places_objects = Place.objects.all()

    for place in places_objects:
        places_geojson["features"].append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.coordinates_lng, place.coordinates_lat],
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.place_id,
                    "detailsUrl": "Non aviable",
                },
            }
        )

    return render(request, "index.html", context={"places_geojson": places_geojson})

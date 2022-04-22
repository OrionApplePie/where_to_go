from django.shortcuts import render
from django.urls import reverse

from places.models import Place


def index(request):
    """Вью главной страницы."""

    places_geojson = {"type": "FeatureCollection", "features": []}

    places = Place.objects.all()

    for place in places:
        places_geojson["features"].append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.coordinates_lng, place.coordinates_lat],
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.slug,
                    "detailsUrl": reverse("places-place-json", args=(place.pk,)),
                },
            }
        )

    return render(request, "index.html", context={"places_geojson": places_geojson})

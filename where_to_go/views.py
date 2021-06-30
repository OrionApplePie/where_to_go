from django.http import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render
from places.models import Image, Place


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


def get_place_json(request, place_id):
    place_obj = get_object_or_404(Place, pk=place_id)
    images_obj_list = get_list_or_404(
        Image.objects.order_by("order_num"), place__pk=place_id
    )

    images_urls = [obj.image.url for obj in images_obj_list]

    obj_json_data = {
        "title": f"{place_obj.title}",
        "imgs": images_urls,
        "description_short": f"{place_obj.description_short}",
        "description_long": f"{place_obj.description_long}",
        "coordinates": {
            "lng": f"{place_obj.coordinates_lng}",
            "lat": f"{place_obj.coordinates_lat}",
        },
    }

    return JsonResponse(
        obj_json_data,
        safe=False,
        json_dumps_params={"ensure_ascii": False, "indent": 2},
    )

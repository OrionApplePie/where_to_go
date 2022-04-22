from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from places.models import Place


def get_place_json(request, place_id):
    """Вью для загрузки данных мест города в формате JSON."""

    place = get_object_or_404(Place, id=place_id)
    images = place.images.all().order_by("order_num")

    images_urls = [obj.image.url for obj in images]

    obj_json_data = {
        "title": place.title,
        "imgs": images_urls,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": f"{place.coordinates_lng}",
            "lat": f"{place.coordinates_lat}",
        },
    }

    return JsonResponse(
        obj_json_data,
        safe=False,
        json_dumps_params={"ensure_ascii": False, "indent": 2},
    )

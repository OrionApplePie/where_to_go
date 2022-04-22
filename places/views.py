from django.http import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404

from places.models import Image, Place


def get_place_json(request, place_id):
    """Вью для загрузки данных мест города в формате JSON."""

    place = get_object_or_404(Place, pk=place_id)
    images_obj_list = get_list_or_404(
        Image.objects.order_by("order_num"), place__pk=place_id
    )

    images_urls = [obj.image.url for obj in images_obj_list]

    obj_json_data = {
        "title": f"{place.title}",
        "imgs": images_urls,
        "description_short": f"{place.description_short}",
        "description_long": f"{place.description_long}",
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

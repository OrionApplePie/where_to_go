import os

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand, CommandError
from places.models import Image, Place
from requests.compat import urlparse

from places.utils import slugify


def save_place_images(place, image_url, order_num):
    filename = os.path.basename(urlparse(image_url).path)
    image = Image(place=place, order_num=order_num)
    img = requests.get(image_url)
    image.image.save(filename, ContentFile(img.content), save=False)
    image.save()


class Command(BaseCommand):
    help = "Load places data from json url command."

    def add_arguments(self, parser):
        parser.add_argument("urls", nargs="+", type=str)

    def handle(self, *args, **options):
        for url in options["urls"]:
            resp = requests.get(url=url)
            try:
                resp_json = resp.json()
            except requests.exceptions.JSONDecodeError:
                self.stdout.write(
                    self.style.NOTICE("url %s don't have json data" % (url))
                )
                continue

            place, created = Place.objects.get_or_create(
                title=resp_json["title"],
                coordinates_lng=resp_json["coordinates"]["lng"],
                coordinates_lat=resp_json["coordinates"]["lat"],
                defaults={
                    "slug": slugify(resp_json["title"]),
                    "description_short": resp_json["description_short"],
                    "description_long": resp_json["description_long"],
                },
            )

            if created:
                for i, image_url in enumerate(resp_json["imgs"], 1):
                    save_place_images(place, image_url=image_url, order_num=i)
                    self.stdout.write(
                        self.style.SUCCESS(
                            "Image %i for place %s saved" % (i, resp_json["title"])
                        )
                    )
                self.stdout.write(
                    self.style.SUCCESS("Place %s created" % (resp_json["title"]))
                )
            else:
                self.stdout.write(
                    self.style.NOTICE(
                        "Place %s already exist in database" % (resp_json["title"])
                    )
                )

import os

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
import requests
from requests.compat import urlparse

from places.models import Image, Place
from places.utils import slugify


def save_place_image(place, image_url, order_num):
    filename = os.path.basename(urlparse(image_url).path)
    image = Image(place=place, order_num=order_num)

    img_response = requests.get(image_url)
    img_response.raise_for_status()

    image.image.save(filename, ContentFile(img_response.content), save=False)
    image.save()


class Command(BaseCommand):
    help = "Load places data from json url command."

    def add_arguments(self, parser):
        parser.add_argument("urls", nargs="+", type=str)

    def handle(self, *args, **options):
        for url in options["urls"]:
            try:
                resp = requests.get(url=url)
                resp.raise_for_status()
            except requests.exceptions.HTTPError as err:
                self.stdout.write(self.style.NOTICE(err))
                continue

            except requests.exceptions.ConnectionError as err:
                self.stdout.write(self.style.NOTICE(err))
                continue

            try:
                place_raw = resp.json()
            except requests.exceptions.JSONDecodeError:
                self.stdout.write(
                    self.style.NOTICE("url %s don't have json data" % (url))
                )
                continue

            place, created = Place.objects.get_or_create(
                title=place_raw["title"],
                coordinates_lng=place_raw["coordinates"]["lng"],
                coordinates_lat=place_raw["coordinates"]["lat"],
                defaults={
                    "slug": slugify(place_raw["title"]),
                    "description_short": place_raw["description_short"],
                    "description_long": place_raw["description_long"],
                },
            )

            if created:
                for i, image_url in enumerate(place_raw["imgs"], 1):
                    try:
                        save_place_image(place, image_url=image_url, order_num=i)
                    except requests.exceptions.HTTPError as err:
                        self.stdout.write(self.style.NOTICE(err))
                        continue
                    except requests.exceptions.ConnectionError as err:
                        self.stdout.write(self.style.NOTICE(err))
                        continue

                    self.stdout.write(
                        self.style.SUCCESS(
                            "Image %i for place %s saved" % (i, place_raw["title"])
                        )
                    )
                self.stdout.write(
                    self.style.SUCCESS("Place %s created" % (place_raw["title"]))
                )
            else:
                self.stdout.write(
                    self.style.NOTICE(
                        "Place %s already exist in database" % (place_raw["title"])
                    )
                )

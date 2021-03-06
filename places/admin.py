from django.contrib import admin
from django.utils.html import format_html

from adminsortable2.admin import SortableInlineAdminMixin

from places.models import Place, Image

IMAGE_MAX_HEIGHT = 200


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image

    fields = ("image", "preview_image", "order_num")

    readonly_fields = [
        "preview_image",
    ]

    def preview_image(self, obj):
        return format_html(
            '<img src="{}" width="{}" />',
            obj.image.url,
            IMAGE_MAX_HEIGHT,
        )

    preview_image.short_description = "Превью"


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]

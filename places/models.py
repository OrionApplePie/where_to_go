from django.db import models
from tinymce.models import HTMLField
import uuid


class Place(models.Model):
    """Модель мест активного отдыха.
    Содержит описание и координаты для карты."""

    title = models.CharField(
        verbose_name="Название",
        max_length=60,
    )

    slug = models.SlugField(
        verbose_name="Символьный идентификатор места",
        max_length=128,
        unique=True,
        default=uuid.uuid4,
    )

    description_short = models.TextField(verbose_name="Короткое описание", blank=True)

    description_long = HTMLField(
        verbose_name="Полное описание",
    )

    coordinates_lng = models.FloatField(
        verbose_name="Долгота",
    )

    coordinates_lat = models.FloatField(
        verbose_name="Широта",
    )

    class Meta:
        verbose_name = "Интересное место города"
        verbose_name_plural = "Интересные места города"
        ordering = ("title",)

    def __str__(self):
        return self.title


class Image(models.Model):
    """Модель картинки места."""

    place = models.ForeignKey(
        to="Place",
        related_name="images",
        on_delete=models.CASCADE,
    )

    order_num = models.PositiveIntegerField(
        verbose_name="Порядковый номер",
    )

    image = models.ImageField(verbose_name="Картинка")

    class Meta:
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"

        ordering = [
            "order_num",
        ]

    def __str__(self):
        return f"{self.order_num} {self.place}"

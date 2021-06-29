from django.db import models


class Place(models.Model):
    """Модель мест активного отдыха.
    Содержит описание и координаты для карты."""

    title = models.CharField(
        verbose_name='Название',
        max_length=60,
        blank=False,
    )

    description_short = models.TextField(
        verbose_name='Короткое описание',
        blank=False,
    )

    description_long = models.TextField(
        verbose_name='Полное описание',
        blank=False
    )

    coordinates_lng = models.FloatField(
        verbose_name='Долгота',
        blank=False,
    )

    coordinates_lat = models.FloatField(
        verbose_name='Широта',
        blank=False,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Интересное место города'
        verbose_name_plural = 'Интересные места города'
        ordering = ('title',)
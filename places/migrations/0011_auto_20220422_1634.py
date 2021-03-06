# Generated by Django 3.1 on 2022-04-22 06:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0010_auto_20220416_1149"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="place",
            name="place_id",
        ),
        migrations.AddField(
            model_name="place",
            name="slug",
            field=models.SlugField(
                default=uuid.uuid4,
                max_length=128,
                null=True,
                verbose_name="Символьный идентификатор места",
            ),
        ),
        migrations.AlterField(
            model_name="place",
            name="description_short",
            field=models.TextField(blank=True, verbose_name="Короткое описание"),
        ),
    ]

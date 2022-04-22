# Generated by Django 3.1 on 2022-04-22 06:54

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0012_auto_20220422_1654"),
    ]

    operations = [
        migrations.AlterField(
            model_name="place",
            name="slug",
            field=models.SlugField(
                default=uuid.uuid4,
                max_length=128,
                unique=True,
                verbose_name="Символьный идентификатор места",
            ),
        ),
    ]
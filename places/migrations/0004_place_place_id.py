# Generated by Django 3.2.4 on 2021-06-29 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20210629_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='place_id',
            field=models.TextField(default='name', verbose_name='id места'),
            preserve_default=False,
        ),
    ]

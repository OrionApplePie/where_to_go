# Generated by Django 3.2.4 on 2021-06-29 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'Картинка', 'verbose_name_plural': 'Картинки'},
        ),
        migrations.AddField(
            model_name='image',
            name='order_num',
            field=models.IntegerField(default=1, verbose_name='Порядковый номер'),
            preserve_default=False,
        ),
    ]

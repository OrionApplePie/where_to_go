# Generated by Django 3.1 on 2022-04-16 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_auto_20210701_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='place',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-14 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendingmachine', '0002_vending_machine_iteminstock_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vending_machine',
            name='image',
            field=models.URLField(default='www.google.com'),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.0.14 on 2021-05-11 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20210511_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress_customer',
            name='address_id',
            field=models.SlugField(null=True),
        ),
    ]
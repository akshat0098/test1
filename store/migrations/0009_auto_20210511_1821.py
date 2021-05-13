# Generated by Django 3.0.14 on 2021-05-11 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0008_auto_20210511_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.Product'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='qty',
            field=models.IntegerField(null=True),
        ),
    ]
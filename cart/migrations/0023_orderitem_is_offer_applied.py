# Generated by Django 4.1.7 on 2023-04-26 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0022_orderitem_offer_alter_order_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='is_offer_applied',
            field=models.BooleanField(default=False),
        ),
    ]
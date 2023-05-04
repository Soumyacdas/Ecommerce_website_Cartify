# Generated by Django 4.1.7 on 2023-04-03 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
        ('cart', '0013_orderitem_ordered_alter_orderitem_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='checkout.address'),
        ),
    ]

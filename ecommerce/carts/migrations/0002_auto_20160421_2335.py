# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('orders', '0001_initial'),
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='order',
            field=models.ForeignKey(blank=True, to='orders.Order', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(to='products.Product'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cartitem',
            name='variation',
            field=models.ForeignKey(blank=True, to='products.Variation', null=True),
            preserve_default=True,
        ),
    ]

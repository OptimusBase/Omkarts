# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_image'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recentviews',
            name='product',
        ),
        migrations.AddField(
            model_name='recentviews',
            name='variation',
            field=models.ForeignKey(blank=True, to='products.Variation', null=True),
            preserve_default=True,
        ),
    ]

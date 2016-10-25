# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_cartitem_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='resend_notification',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='user_notification',
            field=models.CharField(default=b'Created', max_length=128, choices=[(b'Created', b'Created'), (b'Placed', b'Placed'), (b'Confirmed', b'Confirmed'), (b'Cancelled', b'Cancelled'), (b'Shipped', b'Shipped'), (b'Delivered', b'Delivered')]),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='status',
            field=models.CharField(default=b'Created', max_length=128, choices=[(b'Created', b'Created'), (b'Placed', b'Placed'), (b'Confirmed', b'Confirmed'), (b'Cancelled', b'Cancelled'), (b'Shipped', b'Shipped'), (b'Delivered', b'Delivered')]),
        ),
    ]

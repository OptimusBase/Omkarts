# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20160504_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='razor_payment_id',
            field=models.CharField(default=b'', max_length=225, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ordercancellationrequest',
            name='cancel_status',
            field=models.CharField(default=b'', choices=[(b'Refund Initiated', b'Initiated'), (b'Amount Refunded', b'Refunded')], max_length=255, blank=True, null=True, verbose_name=b'Order Status'),
        ),
    ]

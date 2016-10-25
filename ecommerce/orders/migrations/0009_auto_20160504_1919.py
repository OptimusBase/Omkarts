# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20160504_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordercancellationrequest',
            name='cancel_status',
            field=models.CharField(default=b'Not Initiated', max_length=255, verbose_name=b'Order Status', choices=[(b'Refund Not Initiated', b'Not Initiated'), (b'Refund Initiated', b'Initiated'), (b'Amount Refunded', b'Refunded')]),
        ),
    ]

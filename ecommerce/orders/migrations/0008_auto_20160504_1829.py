# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20160504_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordercancellationrequest',
            name='cancel_status',
            field=models.CharField(default=b'Not Initiated', choices=[(b'Refund Not Initiated', b'Not Initiated'), (b'Refund Initiated', b'Initiated'), (b'Amount Refunded', b'Refunded')], max_length=255, blank=True, null=True, verbose_name=b'Order Status'),
        ),
    ]

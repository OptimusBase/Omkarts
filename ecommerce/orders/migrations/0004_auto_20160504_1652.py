# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20160426_1048'),
        ('orders', '0003_ordercancellationrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordercancellationrequest',
            name='variation',
            field=models.ForeignKey(default=b'', to='products.Variation'),
        ),
        migrations.AlterField(
            model_name='ordercancellationrequest',
            name='cancel_order',
            field=models.CharField(default=b'No', help_text=b'Select Yes if you want to cancel the order else select No', max_length=255, verbose_name=b'Cancel Order ?', choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
        ),
        migrations.AlterField(
            model_name='ordercancellationrequest',
            name='cancel_status',
            field=models.CharField(default=b'', max_length=255, verbose_name=b'Order Status', choices=[(b'Refund Initiated', b'Initiated'), (b'Amount Refunded', b'Refunded')]),
        ),
    ]

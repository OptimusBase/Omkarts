# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_remove_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordercancellationrequest',
            name='user_notification',
            field=models.TextField(default=b'', help_text=b'Please give the reason if the order cannot be cancelled', null=True, verbose_name=b'Message for customer.', blank=True),
        ),
        migrations.AlterField(
            model_name='ordercancellationrequest',
            name='cancel_order',
            field=models.CharField(default=b'', choices=[(b'Yes', b'Yes'), (b'No', b'No')], max_length=255, blank=True, help_text=b'Select Yes if you want to cancel the order else select No', null=True, verbose_name=b'Cancel Order ?'),
        ),
        migrations.AlterField(
            model_name='ordercancellationrequest',
            name='cancel_status',
            field=models.CharField(default=b'Refund Not Initiated', max_length=255, verbose_name=b'Order Status', choices=[(b'Refund Not Initiated', b'Not Initiated'), (b'Refund Initiated', b'Refund Initiated'), (b'Amount Refunded', b'Refunded')]),
        ),
    ]

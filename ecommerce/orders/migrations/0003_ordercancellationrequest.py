# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_order_billing_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderCancellationRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reason', models.TextField(verbose_name=b'Reason For Order Cancellation.')),
                ('cancel_order', models.CharField(help_text=b'Select Yes if you want to cancel the order else select No', max_length=255, verbose_name=b'Cancel Order ?', choices=[(b'Yes', b'Yes'), (b'No', b'No')])),
                ('cancel_status', models.CharField(max_length=255, verbose_name=b'Order Status', choices=[(b'Refund Initiated', b'Initiated'), (b'Amount Refunded', b'Refunded')])),
                ('active', models.BooleanField(default=True)),
                ('order', models.OneToOneField(to='orders.Order')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20160504_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordercancellationrequest',
            name='reason',
            field=models.CharField(default=b'', max_length=255, verbose_name=b'Reason For Cancellation.', choices=[(b'Changed My Mind', b'Changed My Mind'), (b'Discovered the same product at a lower price ', b'Discovered the same product at a lower price '), (b"I don't need it any more", b"I don't need it any more"), (b'Product is taking too long to be delivered', b'Product is taking too long to be delivered'), (b'Received damaged product', b'Received damaged product')]),
        ),
    ]

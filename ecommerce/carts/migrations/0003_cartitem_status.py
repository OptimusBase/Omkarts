# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_auto_20160424_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='status',
            field=models.CharField(default=b'Created', max_length=128, choices=[(b'Created', b'Created'), (b'Placed', b'Placed'), (b'Started', b'Started'), (b'Abandoned', b'Abandoned'), (b'Finished', b'Finished')]),
        ),
    ]

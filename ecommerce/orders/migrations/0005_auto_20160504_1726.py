# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20160504_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordercancellationrequest',
            name='other_reason',
            field=models.TextField(default=b'', verbose_name=b'Anything else you would like to tell us?'),
        ),
        migrations.AlterField(
            model_name='ordercancellationrequest',
            name='reason',
            field=models.CharField(default=b'', max_length=255, verbose_name=b'Reason For Cancellation.', choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
        ),
    ]

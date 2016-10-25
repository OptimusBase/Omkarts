# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_auto_20160505_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordercancellationrequest',
            name='user_notification',
            field=models.CharField(default=b'', max_length=128, null=True, blank=True, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
        ),
    ]

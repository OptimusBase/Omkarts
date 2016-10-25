# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20160505_0744'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordercancellationrequest',
            name='resend_notification',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ordercancellationrequest',
            name='user_notification',
            field=models.CharField(default=b'Created', max_length=128, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
        ),
    ]

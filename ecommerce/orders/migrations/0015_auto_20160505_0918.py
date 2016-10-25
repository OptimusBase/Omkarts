# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20160505_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordercancellationrequest',
            name='cancel_order',
            field=models.CharField(default=b'', choices=[(b'Yes', b'Yes'), (b'No', b'No')], max_length=255, blank=True, help_text=b'Select Yes if you want to cancel the order else select No', null=True, verbose_name=b'Cancel Order ?'),
        ),
        migrations.AlterField(
            model_name='ordercancellationrequest',
            name='user_notification',
            field=models.CharField(default=b'', max_length=128, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
        ),
    ]

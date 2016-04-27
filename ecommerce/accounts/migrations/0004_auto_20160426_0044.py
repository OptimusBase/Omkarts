# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20160426_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='name',
            field=models.CharField(default=b'', max_length=120),
        ),
    ]

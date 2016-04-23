# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allcategoryslider',
            name='featured',
        ),
        migrations.RemoveField(
            model_name='categoryslider',
            name='featured',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='featured',
        ),
    ]

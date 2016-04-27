# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='slug',
            field=models.SlugField(default=b'', unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=b'', unique=True),
        ),
        migrations.AlterField(
            model_name='subcategorychild',
            name='slug',
            field=models.SlugField(default=b'', unique=True),
        ),
        migrations.AlterField(
            model_name='subcategoryparent',
            name='slug',
            field=models.SlugField(default=b'', unique=True),
        ),
    ]

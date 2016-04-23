# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='productimage',
            name='thumbnail',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=b'', to='products.Category'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='sub_category_child',
            field=models.ForeignKey(default=b'', to='products.SubCategoryChild'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='sub_category_parent',
            field=models.ForeignKey(default=b'', to='products.SubCategoryParent'),
            preserve_default=True,
        ),
    ]

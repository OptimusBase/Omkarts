# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('product_description', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductFilter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('sub_cat_parent', models.OneToOneField(default=b'', to='products.SubCategoryParent')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductFilterAttributes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('filter_field', models.ForeignKey(default=b'', to='product_description.PdpSpecificationType')),
                ('product_filter', models.ForeignKey(to='product_filters.ProductFilter')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

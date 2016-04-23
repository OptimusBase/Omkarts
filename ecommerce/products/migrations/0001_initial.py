# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('brand_name', models.CharField(max_length=120, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('slug', models.SlugField(unique=True, null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('featured', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BrandConfiguration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('featured', models.BooleanField(default=False)),
                ('order', models.IntegerField(null=True, blank=True)),
                ('brand', models.ForeignKey(blank=True, to='products.Brand', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(max_length=120, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('slug', models.SlugField(unique=True, null=True, blank=True)),
                ('featured', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('image', models.ImageField(default=b'', upload_to=b'products/images')),
                ('slug', models.SlugField(unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('brand', models.ForeignKey(default=b'', to='products.Brand')),
                ('category', models.ForeignKey(blank=True, to='products.Category', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'Variation/images')),
                ('featured', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubCategoryChild',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sub_cat_child_name', models.CharField(max_length=120, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('slug', models.SlugField(unique=True, null=True, blank=True)),
                ('featured', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubCategoryParent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sub_cat_parent_name', models.CharField(max_length=120, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('slug', models.SlugField(unique=True, null=True, blank=True)),
                ('featured', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(blank=True, to='products.Category', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('color', models.CharField(max_length=120, null=True, blank=True)),
                ('storage', models.CharField(max_length=120, null=True, blank=True)),
                ('screen_size', models.CharField(max_length=120, null=True, blank=True)),
                ('quantity', models.IntegerField(null=True, blank=True)),
                ('price', models.DecimalField(null=True, max_digits=100, decimal_places=2, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(to='products.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='subcategorychild',
            name='sub_category_parent',
            field=models.ForeignKey(blank=True, to='products.SubCategoryParent', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='productimage',
            name='variation',
            field=models.ForeignKey(blank=True, to='products.Variation', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category_child',
            field=models.ForeignKey(blank=True, to='products.SubCategoryChild', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category_parent',
            field=models.ForeignKey(blank=True, to='products.SubCategoryParent', null=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together=set([('title', 'slug')]),
        ),
        migrations.AddField(
            model_name='brandconfiguration',
            name='sub_category_parent',
            field=models.ForeignKey(blank=True, to='products.SubCategoryParent', null=True),
            preserve_default=True,
        ),
    ]

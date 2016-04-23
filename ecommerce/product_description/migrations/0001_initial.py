# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PdpDescription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(help_text=b'Enter Product Description.', null=True, verbose_name=b'Description', blank=True)),
                ('active', models.BooleanField(default=True)),
                ('variation', models.ForeignKey(blank=True, to='products.Variation', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PdpFeatured',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('featured_image', models.ImageField(help_text=b'Enter Product Featured Image.', upload_to=b'product_description/images/featured', null=True, verbose_name=b'Featured Image', blank=True)),
                ('header', models.TextField(help_text=b'Enter Product Featured Header.', null=True, verbose_name=b'Featured header', blank=True)),
                ('description', models.TextField(help_text=b'Enter Product Featured description.', null=True, verbose_name=b'Featured description', blank=True)),
                ('order', models.IntegerField(help_text=b'The product featured item will be shown in this order.', null=True, verbose_name=b'Featured Order', blank=True)),
                ('active', models.BooleanField(default=True)),
                ('variation', models.ForeignKey(blank=True, to='products.Variation', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PdpKeyFeature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('icon_type', models.CharField(default=b'Google', help_text=b'Enter Key Feature Icon Type. Select the option of which you want icons of.', max_length=225, verbose_name=b'Icon type', choices=[(b'Google', b'Google'), (b'Font-Awesome', b'Font-Awesome')])),
                ('icon_class', models.CharField(default=b'', max_length=255, blank=True, help_text=b'Enter Key Feature Icon Class. This is required only if you want Font-Awesome icons', null=True, verbose_name=b'Icon Class')),
                ('title', models.TextField(help_text=b'Enter Key Feature Text.', null=True, verbose_name=b'Key Feature Text', blank=True)),
                ('active', models.BooleanField(default=True)),
                ('variation', models.ForeignKey(blank=True, to='products.Variation', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PdpPhysicalFeature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key_feature_image', models.ImageField(help_text=b'Enter Product Physical Feature Image.', upload_to=b'product_description/images/physical_feature', null=True, verbose_name=b'Physical Feature Image', blank=True)),
                ('active', models.BooleanField(default=True)),
                ('variation', models.ForeignKey(blank=True, to='products.Variation', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PdpSpecification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('specification_value', models.CharField(help_text=b'Enter Product Specification value. Example "Apple" ', max_length=255, null=True, verbose_name=b'Specification value', blank=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PdpSpecificationType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('specification_type', models.CharField(help_text=b'Enter Product Specification type. Example "Brand" ', max_length=255, null=True, verbose_name=b'Specification type', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pdpspecification',
            name='specification_type',
            field=models.ForeignKey(default=b'', to='product_description.PdpSpecificationType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pdpspecification',
            name='variation',
            field=models.ForeignKey(blank=True, to='products.Variation', null=True),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailConfirmed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activation_key', models.CharField(max_length=200)),
                ('confirmed', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EmailMarketingSignUp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=75)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RecentViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(blank=True, to='products.Product', null=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120, null=True, blank=True)),
                ('address', models.CharField(max_length=120)),
                ('address2', models.CharField(max_length=120, null=True, blank=True)),
                ('city', models.CharField(max_length=120)),
                ('state', models.CharField(default=b'', max_length=120, null=True, blank=True, choices=[(b'KA', b'Karnataka'), (b'AP', b'Andhra Pradesh'), (b'KL', b'Kerala'), (b'TN', b'Tamil Nadu'), (b'MH', b'Maharashtra'), (b'UP', b'Uttar Pradesh'), (b'GA', b'Goa'), (b'GJ', b'Gujarat'), (b'RJ', b'Rajasthan'), (b'HP', b'Himachal Pradesh'), (b'JK', b'Jammu and Kashmir'), (b'TG', b'Telangana'), (b'AR', b'Arunachal Pradesh'), (b'AS', b'Assam'), (b'BR', b'Bihar'), (b'CG', b'Chattisgarh'), (b'HR', b'Haryana'), (b'JH', b'Jharkhand'), (b'MP', b'Madhya Pradesh'), (b'MN', b'Manipur'), (b'ML', b'Meghalaya'), (b'MZ', b'Mizoram'), (b'NL', b'Nagaland'), (b'OR', b'Orissa'), (b'PB', b'Punjab'), (b'SK', b'Sikkim'), (b'TR', b'Tripura'), (b'UA', b'Uttarakhand'), (b'WB', b'West Bengal'), (b'AN', b'Andaman and Nicobar'), (b'CH', b'Chandigarh'), (b'DN', b'Dadra and Nagar Haveli'), (b'DD', b'Daman and Diu'), (b'DL', b'Delhi'), (b'LD', b'Lakshadweep'), (b'PY', b'Pondicherry')])),
                ('country', models.CharField(max_length=120)),
                ('zipcode', models.CharField(max_length=25)),
                ('phone', models.CharField(default=b'', max_length=120)),
                ('shipping', models.BooleanField(default=True)),
                ('billing', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated', '-timestamp'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserDefaultAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('billing', models.ForeignKey(related_name='user_address_billing_default', blank=True, to='accounts.UserAddress', null=True)),
                ('shipping', models.ForeignKey(related_name='user_address_shipping_default', blank=True, to='accounts.UserAddress', null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserInformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120, null=True, blank=True)),
                ('gender', models.CharField(max_length=8, choices=[(b'Male', b'Male'), (b'Female', b'Female')])),
                ('country', models.CharField(max_length=8, choices=[(b'India', b'India')])),
                ('birthdate', models.DateField(null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserStripe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stripe_id', models.CharField(max_length=128, null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(blank=True, to='products.Product', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('variation', models.ForeignKey(blank=True, to='products.Variation', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

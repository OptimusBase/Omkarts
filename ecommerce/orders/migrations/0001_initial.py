# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_id', models.CharField(default=b'ABC', unique=True, max_length=128)),
                ('status', models.CharField(default=b'Created', max_length=128, choices=[(b'Created', b'Created'), (b'Placed', b'Placed'), (b'Started', b'Started'), (b'Abandoned', b'Abandoned'), (b'Finished', b'Finished')])),
                ('payment', models.CharField(default=b'Not Paid', max_length=128, choices=[(b'Not Paid', b'Not Paid'), (b'Cash on delivery', b'Cash on delivery'), (b'Paid', b'Paid')])),
                ('sub_total', models.DecimalField(default=10.99, max_digits=100, decimal_places=2)),
                ('tax_total', models.DecimalField(default=0.0, max_digits=100, decimal_places=2)),
                ('final_total', models.DecimalField(default=10.99, max_digits=100, decimal_places=2)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('billing_address', models.ForeignKey(related_name='billing_address', default=1, to='accounts.UserAddress')),
                ('cart', models.ForeignKey(blank=True, to='carts.Cart', null=True)),
                ('shipping_address', models.ForeignKey(related_name='shipping_address', default=1, to='accounts.UserAddress')),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

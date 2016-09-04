# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AliPayDPN',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notify_time', models.DateTimeField(blank=True, null=True)),
                ('notify_type', models.CharField(blank=True, null=True, max_length=32)),
                ('notify_id', models.CharField(blank=True, null=True, max_length=64)),
                ('sign_type', models.CharField(blank=True, null=True, max_length=3)),
                ('sign', models.CharField(blank=True, null=True, max_length=64)),
                ('out_trade_no', models.CharField(blank=True, null=True, max_length=64)),
                ('subject', models.CharField(blank=True, null=True, max_length=256)),
                ('payment_type', models.CharField(blank=True, null=True, max_length=4)),
                ('trade_no', models.CharField(blank=True, null=True, max_length=64)),
                ('trade_status', models.CharField(blank=True, null=True, max_length=32)),
                ('gmt_create', models.DateTimeField(blank=True, null=True)),
                ('gmt_payment', models.DateTimeField(blank=True, null=True)),
                ('refund_status', models.CharField(blank=True, null=True, max_length=32)),
                ('gmt_refund', models.DateTimeField(blank=True, null=True)),
                ('seller_email', models.CharField(blank=True, null=True, max_length=100)),
                ('buyer_email', models.CharField(blank=True, null=True, max_length=100)),
                ('seller_id', models.CharField(blank=True, null=True, max_length=30)),
                ('buyer_id', models.CharField(blank=True, null=True, max_length=30)),
                ('price', models.FloatField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('total_fee', models.FloatField(blank=True, null=True)),
                ('discount', models.FloatField(blank=True, null=True)),
                ('body', models.CharField(blank=True, null=True, max_length=400)),
                ('is_total_fee_adjust', models.CharField(blank=True, null=True, max_length=1)),
                ('use_coupon', models.CharField(blank=True, null=True, max_length=1)),
                ('ipaddress', models.GenericIPAddressField(blank=True, null=True)),
                ('flag', models.BooleanField(default=False, blank=True)),
                ('flag_code', models.CharField(max_length=16, blank=True)),
                ('flag_info', models.TextField(blank=True)),
                ('query', models.TextField(blank=True)),
                ('response', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('gmt_close', models.DateTimeField(blank=True, null=True)),
                ('extra_common_param', models.CharField(blank=True, null=True, max_length=256)),
                ('out_channel_type', models.CharField(blank=True, null=True, max_length=256)),
                ('out_channel_amount', models.CharField(blank=True, null=True, max_length=256)),
                ('out_channel_inst', models.CharField(blank=True, null=True, max_length=256)),
            ],
            options={
                'db_table': 'alipay_dpn',
                'verbose_name': 'AliPay DPN',
            },
            bases=(models.Model,),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20150329_0509'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='sensor',
            field=models.ForeignKey(default=None, to='main.Tsensor', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='room',
            name='temperature_current',
            field=models.OneToOneField(related_name='+', null=True, default=None, to='main.Temperature'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='room',
            name='temperature_high',
            field=models.OneToOneField(related_name='+', null=True, default=None, to='main.Temperature'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='room',
            name='temperature_low',
            field=models.OneToOneField(related_name='+', null=True, default=None, to='main.Temperature'),
            preserve_default=True,
        ),
    ]

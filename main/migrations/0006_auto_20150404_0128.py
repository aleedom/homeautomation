# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20150404_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='temperature_current',
            field=models.OneToOneField(related_name='+', null=True, default=None, blank=True, to='main.Temperature'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='room',
            name='temperature_high',
            field=models.OneToOneField(related_name='+', null=True, default=None, blank=True, to='main.Temperature'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='room',
            name='temperature_low',
            field=models.OneToOneField(related_name='+', null=True, default=None, blank=True, to='main.Temperature'),
            preserve_default=True,
        ),
    ]

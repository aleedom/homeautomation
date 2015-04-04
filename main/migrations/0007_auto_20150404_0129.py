# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20150404_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='sensor',
            field=models.ForeignKey(default=None, blank=True, to='main.Tsensor', null=True),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150320_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tsensor',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150320_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tsensor',
            name='active',
        ),
        migrations.AlterField(
            model_name='tsensor',
            name='serial',
            field=models.CharField(max_length=14, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
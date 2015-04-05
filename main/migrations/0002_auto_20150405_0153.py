# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='serial',
            field=models.CharField(max_length=16, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
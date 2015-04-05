# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DecimalField(max_digits=6, decimal_places=3)),
                ('time', models.DateTimeField()),
                ('data_type', models.IntegerField(default=1, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('vent_state', models.IntegerField(default=None, null=True)),
                ('humidity_current', models.OneToOneField(related_name='+', null=True, default=None, blank=True, to='main.Data')),
                ('temperature_current', models.OneToOneField(related_name='+', null=True, default=None, blank=True, to='main.Data')),
                ('temperature_high', models.OneToOneField(related_name='+', null=True, default=None, blank=True, to='main.Data')),
                ('temperature_low', models.OneToOneField(related_name='+', null=True, default=None, blank=True, to='main.Data')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('serial', models.CharField(max_length=14, serialize=False, primary_key=True)),
                ('room_id', models.ForeignKey(default=None, blank=True, to='main.Room', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='data',
            name='room_id',
            field=models.ForeignKey(to='main.Room'),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Infraccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ACTAS_ANULADAS', models.CharField(max_length=32, blank=True)),
                ('ANIO', models.IntegerField(null=True, blank=True)),
                ('AV_JR_CALLE', models.CharField(max_length=128, blank=True)),
                ('CDRA', models.IntegerField(null=True, blank=True)),
                ('COD_RUTA', models.CharField(max_length=16, blank=True)),
                ('CODIGO_INFRACCION', models.CharField(max_length=16, blank=True)),
                ('CONDUCTOR', models.CharField(max_length=64, blank=True)),
                ('CONDUCTOR_NOMBRES', models.CharField(max_length=64, blank=True)),
                ('DISTRITO', models.CharField(max_length=64, blank=True)),
                ('EMPRESA', models.CharField(max_length=128, blank=True)),
                ('EMPRESA1', models.CharField(max_length=128, blank=True)),
                ('FECHA', models.DateField(null=True, blank=True)),
                ('HORA', models.TimeField(null=True, blank=True)),
                ('HORA1', models.CharField(max_length=16, blank=True)),
                ('INSPECTOR', models.CharField(max_length=64, blank=True)),
                ('INSPECTOR1', models.CharField(max_length=64, blank=True)),
                ('LUGAR', models.CharField(max_length=128, blank=True)),
                ('LUGAR1', models.CharField(max_length=128, blank=True)),
                ('MES', models.IntegerField(null=True, blank=True)),
                ('NRO', models.IntegerField(null=True, blank=True)),
                ('NRO_ACTA_DE_CONTROL', models.CharField(max_length=32, blank=True)),
                ('NRO_DE_LICENCIA', models.CharField(max_length=32, blank=True)),
                ('PLACA_DE_RODAJE', models.CharField(max_length=32, blank=True)),
                ('SITUACION_DEL_ACTA', models.CharField(max_length=32, blank=True)),
                ('TENOR_INFRACCION', models.CharField(max_length=128, blank=True)),
                ('TENOR_INFRACCION1', models.CharField(max_length=128, blank=True)),
            ],
            options={
                'verbose_name': 'Infraccion',
                'verbose_name_plural': 'Infraciones',
            },
        ),
    ]

# -*- encoding: utf-8 -*-
from django.contrib import admin
from api.models import Infraccion


class InfraccionAdmin(admin.ModelAdmin):
    list_display = (
        'FECHA',
        'HORA',
        'ANIO',
        'ACTAS_ANULADAS',
        'CDRA',
        'AV_JR_CALLE',
        'COD_RUTA',
        'CODIGO_INFRACCION',
        'CONDUCTOR',
        'CONDUCTOR_NOMBRES',
        'DISTRITO',
        'EMPRESA',
        'EMPRESA1',
        'HORA1',
        'INSPECTOR',
        'INSPECTOR1',
        'LUGAR',
        'LUGAR1',
        'MES',
        'NRO',
        'NRO_ACTA_DE_CONTROL',
        'NRO_DE_LICENCIA',
        'PLACA_DE_RODAJE',
        'SITUACION_DEL_ACTA',
        'TENOR_INFRACCION',
        'TENOR_INFRACCION1',
    )

admin.site.register(Infraccion, InfraccionAdmin)

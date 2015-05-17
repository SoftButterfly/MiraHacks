# -*- encoding: utf-8 -*-
from django.db import models


class Infraccion(models.Model):
    Fields = (
        'ACTAS_ANULADAS',
        'ANIO',
        'AV_JR_CALLE',
        'CDRA',
        'COD_RUTA',
        'CODIGO_INFRACCION',
        'CONDUCTOR',
        'CONDUCTOR_NOMBRES',
        'DISTRITO',
        'EMPRESA',
        'EMPRESA1',
        'FECHA',
        'HORA',
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

    ACTAS_ANULADAS = models.CharField(max_length=32, blank=True)
    ANIO = models.IntegerField(blank=True, null=True)
    AV_JR_CALLE = models.CharField(max_length=128, blank=True)
    CDRA = models.IntegerField(blank=True, null=True)
    COD_RUTA = models.CharField(max_length=16, blank=True)
    CODIGO_INFRACCION = models.CharField(max_length=16, blank=True)
    CONDUCTOR = models.CharField(max_length=64, blank=True)
    CONDUCTOR_NOMBRES = models.CharField(max_length=64, blank=True)
    DISTRITO = models.CharField(max_length=64, blank=True)
    EMPRESA = models.CharField(max_length=128, blank=True)
    EMPRESA1 = models.CharField(max_length=128, blank=True)
    FECHA = models.DateField(blank=True, null=True)
    HORA = models.TimeField(blank=True, null=True)
    HORA1 = models.CharField(max_length=16, blank=True)
    INSPECTOR = models.CharField(max_length=64, blank=True)
    INSPECTOR1 = models.CharField(max_length=64, blank=True)
    LUGAR = models.CharField(max_length=128, blank=True)
    LUGAR1 = models.CharField(max_length=128, blank=True)
    MES = models.IntegerField(blank=True, null=True)
    NRO = models.IntegerField(blank=True, null=True)
    NRO_ACTA_DE_CONTROL = models.CharField(max_length=32, blank=True)
    NRO_DE_LICENCIA = models.CharField(max_length=32, blank=True)
    PLACA_DE_RODAJE = models.CharField(max_length=32, blank=True)
    SITUACION_DEL_ACTA = models.CharField(max_length=32, blank=True)
    TENOR_INFRACCION = models.CharField(max_length=128, blank=True)
    TENOR_INFRACCION1 = models.CharField(max_length=128, blank=True)

    class Meta:
        verbose_name = "Infraccion"
        verbose_name_plural = "Infraciones"

    def __unicode__(self):
        return u"Objeto Infracción: {0:}, {1:} - {2:}".format(self.NRO, self.PLACA_DE_RODAJE, self.CONDUCTOR)

    def __str__(self):
        return "Objeto Infracción: {0:}, {1:} - {2:}".format(self.NRO, self.PLACA_DE_RODAJE, self.CONDUCTOR)

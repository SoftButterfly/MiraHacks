# -*- encoding: utf-8 -*-
from rest_framework import serializers
from api.models import Infraccion


class InfraccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infraccion
        fields = (
            "HORA",
            "ANIO",
            "FECHA",
            "NRO_DE_LICENCIA",
            "EMPRESA1",
            "NRO_ACTA_DE_CONTROL",
            "TENOR_INFRACCION1",
            "EMPRESA",
            "PLACA_DE_RODAJE",
            "CONDUCTOR",
            "CODIGO_INFRACCION",
            "ACTAS_ANULADAS",
            "HORA1",
            "INSPECTOR",
            "CONDUCTOR_NOMBRES",
            "COD_RUTA",
            "LUGAR1",
            "CDRA",
            "LUGAR",
            "INSPECTOR1",
            "NRO",
            "AV_JR_CALLE",
            "SITUACION_DEL_ACTA",
            "MES",
            "TENOR_INFRACCION",
            "DISTRITO",
        )

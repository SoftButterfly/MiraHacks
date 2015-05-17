from django.http import HttpResponse

from rest_framework.views import APIView

from api.models import Infraccion
from api.serializers import InfraccionSerializer

import urllib2 as urllib
import json

from django.core.serializers.json import DjangoJSONEncoder


class infraciones(APIView):
    def get(self, request):
        response = '{}'

        if request.GET:
            response = {}

            if ["group_by"] == request.GET.keys():
                if request.GET["group_by"] in Infraccion.Fields:
                    criteria = request.GET["group_by"]
                    queryset = Infraccion.objects.all()
                    queryset = InfraccionSerializer(queryset, many=True)
                    keys = [item[criteria] for item in queryset.data]
                    keys = set(keys)
                    keys = list(keys)

                    response = {}

                    for key in keys:
                        response[key] = Infraccion.objects.filter(**{criteria: key}).count()

            elif request.GET.keys() in (["group_by", "sub_group_by"], ["sub_group_by", "group_by"]):
                if request.GET["group_by"] in Infraccion.Fields and request.GET["sub_group_by"] in Infraccion.Fields:
                    criteria = request.GET["group_by"]
                    queryset = Infraccion.objects.all()
                    queryset = InfraccionSerializer(queryset, many=True)
                    keys = [item[criteria] for item in queryset.data]
                    keys = set(keys)
                    keys = list(keys)

                    print keys

                    subcriteria = request.GET["sub_group_by"]
                    queryset = Infraccion.objects.all()
                    queryset = InfraccionSerializer(queryset, many=True)
                    subkeys = [item[subcriteria] for item in queryset.data]
                    subkeys = set(subkeys)
                    subkeys = list(subkeys)

                    print subkeys

                    response = {}

                    for key in keys:
                        response[key] = {}

                        for subkey in subkeys:
                            response[key][subkey] = Infraccion.objects.filter(**{criteria: key}).filter(**{subcriteria: subkey}).count()

            response = json.dumps(response, indent=4, cls=DjangoJSONEncoder)

        return HttpResponse(response, content_type='application/json')


class geocode(APIView):
    def get(self, request):
        response = '{}'

        if request.GET:
            urlBase = 'http://maps.googleapis.com/maps/api/geocode/json?'
            for key, value in request.GET.items():
                urlBase = urlBase + key + '=' + value + '&'

            try:
                response = urllib.urlopen(urlBase.replace(' ', '+'))
                response = response.read()
                response = json.loads(response)
                response = json.dumps(response, indent=4, cls=DjangoJSONEncoder)
            except Exception as ex:
                print ex

        return HttpResponse(response, content_type='application/json')


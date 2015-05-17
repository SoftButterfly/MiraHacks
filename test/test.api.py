from api.models import Infraccion
import urllib2 as urllib
import json
import datetime


oauth_api_key = 'f0a484d04388faa9d419deec773d56d06f238024'
guid = 'INFRA-31368'

url = 'http://miraflores.cloudapi.junar.com/datastreams/invoke/{0:}?auth_key={1:}&output=json_array'
url = url.format(guid, oauth_api_key)

request = urllib.urlopen(url)

textResponse = request.read()

jsonResponse = json.loads(textResponse)

data = jsonResponse['result']

keys = []

dictData = []

for i, row in enumerate(data):
    if i == 0:
        keys = [item.replace('-', '_') for item in row]
    else:
        dictData.append(dict(zip(keys, row)))

for i, item in enumerate(dictData):
    dt = item["FECHA"] + ' ' + item["HORA"]
    try:
        dt = datetime.datetime.strptime(dt, "%d/%m/%Y %H:%M")
        item["HORA"] = dt.time()
    except:
        dt = datetime.datetime.strptime(dt, "%d/%m/%Y ")
        item["HORA"] = None
    item["FECHA"] = dt.date()

    try:
        item["ANIO"] = int(item["ANIO"])
    except:
        item["ANIO"] = None

    try:
        item["CDRA"] = int(item["CDRA"])
    except:
        item["CDRA"] = None

    try:
        item["MES"] = int(item["MES"])
    except:
        item["MES"] = None

    try:
        item["NRO"] = int(item["NRO"])
    except:
        item["NRO"] = None

    a = Infraccion(**item)
    a.save()
    print i

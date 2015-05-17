import urllib2 as urllib
import json

url = 'http://miraflores.cloudapi.junar.com/datastreams/invoke/{0:}?auth_key={1:}&output=json_array'

oauth_api_key = 'f0a484d04388faa9d419deec773d56d06f238024'

guids = (
    "TIPO-DE-VIA",
    "CALLE",
    "EMPRE-DE-TRANS-10638",
    "UBICA",
    "TIPO-DE-INFRA-61965",
    "INFRA-POR-UBICA-HORA",
    "INFRA-POR-UBICA",
    "RANKI-DE-EMPRE-INFRA",
    "AUXIL-EFECT-POR-TURNO",
    "FOTO-PAPEL-EMITI",
    "CAMPA-YO-ESTAC-PESIM",
    "INFRA-31368",
)

for guid in guids:
    guidUrl = url.format(guid, oauth_api_key)

    print "GUID: {0:}".format(guid)
    print "URL : {0:}".format(guidUrl)

    request = urllib.urlopen(guidUrl)
    textResponse = request.read()
    jsonResponse = json.loads(textResponse)

    data = jsonResponse['result']

    keys = []

    dictData = []

    keys = [item.replace('-', '_') for item in data[0]]

    sampleDict = dict(zip(keys, data[1]))

    json.dumps(sampleDict, indent=4)

    print "File: {0:}".format(sampleJSONStr)
    print '*'*30

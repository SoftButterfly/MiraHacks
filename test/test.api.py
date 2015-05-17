import urllib2 as urllib
import json
import pandas
import datetime

oauth_api_key = '14ce3b2e1d6a7a361a167f2d27c7d69209e39df4'
guid = 'INFRA-31368'

url = 'http://miraflores.cloudapi.junar.com/datastreams/invoke/{0:}?auth_key={1:}&output=json_array'
url = url.format(guid, oauth_api_key)

request = urllib.urlopen(url)

textResponse = request.read()

jsonResponse = json.loads(textResponse)

data = jsonResponse['result'] 

keys = []

dictData = []

for i,row in enumerate(data):
	if i == 0:
		keys = [item.replace('-', '_') for item in row]

	else:
		dictData.append(dict(zip(keys,row)))

dates = [item[u'FECHA'] + ' ' + item[u'HORA'] for item in dictData]

datesAux = []

for i, item in enumerate(dates):
	try:
		datesAux.append(datetime.datetime.strptime(item, '%d/%m/%Y %H:%M'))
	except:
		pass

dates = datesAux

frequency = [1]*len(dates)

dataSet = pandas.Series(frequency, index=dates)
dataSet.asfreq('M')

print dataSet
dummy=raw_input('')

def cumulativeFrequency(x):
	return sum(x)

dataSet.resample('H', how='cumulativeFrequency', axis=0)

print dataSet
dummy=raw_input('')




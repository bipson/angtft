import json
from time import strptime, mktime
from datetime import datetime
import dateutil.parser
from numpy import mean, sqrt, square, arange
from importer import Importer
from csvimporter import CSVImporter
from model import RMSDelay, RMSDelayEncoder

# time_format = "%Y-%m-%dT%H:%M:%S.%f+0100"

i = Importer()

i.loadRBLList()

print "Will now call Importer.request()..."
try:
  monitors = i.request()
  request_time = datetime.now()
except:
  print "ERROR: Could not issue request to WL!"
  raise
  exit(0)

# print json.dumps(message)

# message = json.loads("{\"message\": {\"messageCode\": 1, \"serverTime\": \"2014-11-19T11:34:41.870+0100\", \"value\": \"OK\"}, \"data\": {\"monitors\": [{\"locationStop\": {\"geometry\": {\"type\": \"Point\", \"coordinates\": [16.349198741357, 48.2249564556775]}, \"type\": \"Feature\", \"properties\": {\"name\": \"60201510\", \"title\": \"W\u00e4hringer Stra\u00dfe-Volksoper\", \"municipality\": \"Wien\", \"municipalityId\": 90000, \"coordName\": \"WGS84\", \"attributes\": {\"rbl\": 147}, \"type\": \"stop\"}}, \"lines\": [{\"direction\": \"R\", \"towards\": \"Schottentor U\", \"name\": \"40\", \"richtungsId\": \"1\", \"trafficjam\": false, \"departures\": {\"departure\": [{\"departureTime\": {\"timePlanned\": \"2014-11-19T11:41:00.000+0100\", \"countdown\": 7, \"timeReal\": \"2014-11-19T11:42:21.000+0100\"}}, {\"departureTime\": {\"timePlanned\": \"2014-11-19T11:48:00.000+0100\", \"countdown\": 13, \"timeReal\": \"2014-11-19T11:48:30.000+0100\"}, \"vehicle\": {\"direction\": \"R\", \"towards\": \"Schottentor U\", \"name\": \"40\", \"linienId\": 140, \"richtungsId\": \"1\", \"trafficjam\": false, \"barrierFree\": true, \"realtimeSupported\": true, \"type\": \"ptTram\"}}, {\"departureTime\": {\"timePlanned\": \"2014-11-19T11:56:00.000+0100\", \"countdown\": 21, \"timeReal\": \"2014-11-19T11:56:00.000+0100\"}}, {\"departureTime\": {\"timePlanned\": \"2014-11-19T12:03:00.000+0100\", \"countdown\": 28, \"timeReal\": \"2014-11-19T12:03:30.000+0100\"}}, {\"departureTime\": {\"timePlanned\": \"2014-11-19T12:11:00.000+0100\", \"countdown\": 36, \"timeReal\": \"2014-11-19T12:11:00.000+0100\"}}, {\"departureTime\": {\"timePlanned\": \"2014-11-19T12:18:00.000+0100\", \"countdown\": 43, \"timeReal\": \"2014-11-19T12:18:30.000+0100\"}, \"vehicle\": {\"direction\": \"R\", \"towards\": \"Schottentor U\", \"name\": \"40\", \"linienId\": 140, \"richtungsId\": \"1\", \"trafficjam\": false, \"barrierFree\": true, \"realtimeSupported\": true, \"type\": \"ptTram\"}}, {\"departureTime\": {\"timePlanned\": \"2014-11-19T12:26:00.000+0100\", \"countdown\": 51, \"timeReal\": \"2014-11-19T12:26:00.000+0100\"}}, {\"departureTime\": {\"timePlanned\": \"2014-11-19T12:33:00.000+0100\", \"countdown\": 58, \"timeReal\": \"2014-11-19T12:33:30.000+0100\"}}, {\"departureTime\": {\"timePlanned\": \"2014-11-19T12:41:00.000+0100\", \"countdown\": 66}}]}, \"barrierFree\": false, \"realtimeSupported\": true, \"lineId\": 140, \"type\": \"ptTram\"}]}, {\"locationStop\": {\"geometry\": {\"type\": \"Point\", \"coordinates\": [16.349198741357, 48.2249564556775]}, \"type\": \"Feature\", \"properties\": {\"name\": \"60201510\", \"title\": \"W\u00e4hringer Stra\u00dfe-Volksoper\", \"municipality\": \"Wien\", \"municipalityId\": 90000, \"coordName\": \"WGS84\", \"attributes\": {\"rbl\": 147}, \"type\": \"stop\"}}, \"lines\": [{\"direction\": \"R\", \"towards\": \"Schottentor U\", \"name\": \"41\", \"richtungsId\": \"1\", \"trafficjam\": false, \"departures\": {\"departure\": [{\"departureTime\": {\"timePlanned\": \"2014-11-19T11:37:00.000+0100\", \"countdown\": 2, \"timeReal\": \"2014-11-19T11:37:30.000+0100\"}}, {\"departureTime\": {\"timePlanned\": \"2014-11-19T11:45:00.000+0100\", \"countdown\": 9, \"timeReal\": \"2014-11-19T11:44:26.000+0100\"}, \"vehicle\": {\"direction\": \"R\", \"towards\": \"Schottentor U\", \"name\": \"41\", \"linienId\": 141, \"richtungsId\": \"1\", \"trafficjam\": false, \"barrierFree\": true, \"realtimeSupported\": true, \"type\": \"ptTram\"}}, {\"departureTime\": {\"timePlanned\": \"2014-11-19T11:52:00.000+0100\", \"countdown\": 17, \"timeReal\": \"2014-11-19T11:52:30.000+0100\"}, \"vehicle\": {\"direction\": \"R\", \"towards\": \"Schottentor U\", \"name\": \"41\", \"linienId\": 141, \"richtungsId\": \"1\", \"trafficjam\": false, \"barrierFree\": true, \"realtimeSupported\": true, \"type\": \"ptTram\"}}, {\"departureTime\": {\"timePlanned\": \"2014-11-19T12:00:00.000+0100\", \"countdown\": 25, \"timeReal\": \"2014-11-19T12:00:00.000+0100\"}}, {\"departureTime\": {\"timePlanned\": \"2014-11-19T12:07:00.000+0100\", \"countdown\": 32, \"timeReal\": \"2014-11-19T12:07:30.000+0100\"}, \"vehicle\": {\"direction\": \"R\", \"towards\": \"Schottentor U\", \"name\": \"41\", \"linienId\": 141, \"richtungsId\": \"1\", \"trafficjam\": false, \"barrierFree\": true, \"realtimeSupported\": true, \"type\": \"ptTram\"}}, {\"departureTime\": {\"timePlanned\": \"2014-11-19T12:15:00.000+0100\", \"countdown\": 40, \"timeReal\": \"2014-11-19T12:15:00.000+0100\"}}, {\"departureTime\": {\"timePlanned\": \"2014-11-19T12:22:00.000+0100\", \"countdown\": 47, \"timeReal\": \"2014-11-19T12:22:30.000+0100\"}}, {\"departureTime\": {\"timePlanned\": \"2014-11-19T12:30:00.000+0100\", \"countdown\": 55, \"timeReal\": \"2014-11-19T12:30:00.000+0100\"}}, {\"departureTime\": {\"timePlanned\": \"2014-11-19T12:37:00.000+0100\", \"countdown\": 62}}]}, \"barrierFree\": false, \"realtimeSupported\": true, \"lineId\": 141, \"type\": \"ptTram\"}]}]}}")

print "Numbers of monitors received: ", len(monitors)

delays = list()

for monitor in monitors:

  coordinates = monitor['locationStop']['geometry']['coordinates']
  latitude = coordinates[1]
  longitude = coordinates[0]
  title = monitor['locationStop']['properties']['title'].encode('utf-8')

  for line in monitor['lines']:
    diffs = list()
    for departures in line['departures']['departure'][:2]:
      departureTime = departures['departureTime']
      # print departureTime
      # exit(0)
      # TODO skip entries more than x minutes into the future

      # skip entries without one of either timestamps
      if 'timePlanned' in departureTime and 'timeReal' in departureTime:
        planned = dateutil.parser.parse(departureTime['timePlanned'])
        real = dateutil.parser.parse(departureTime['timeReal'])
        # real = mktime(strptime(departureTime['timeReal'], time_format))
        diffs.append((real - planned).total_seconds())

    if diffs:
      # print title, 'Line: ' + line['name'].encode('utf-8'), 'towards', line['towards'].encode('utf-8')
      rms = round(sqrt(mean(square(diffs))))
      delays.append(RMSDelay(latitude, longitude, rms, request_time))
      # print 'RMS of delays:', rms

with open("data/delays.json", "w") as f:
  #json.dump([i.__dict__ for i in delays], f, cls=RMSDelayEncoder)
  json.dump([i.__dict__ for i in delays], f)


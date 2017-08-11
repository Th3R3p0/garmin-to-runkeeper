import json
import datetime

with open('garmin.json', 'r') as f:
    d = json.load(f)

t = datetime.datetime.utcnow()

print('<?xml version="1.0" encoding="UTF-8"?>\n'
      '<gpx \n'
      'version="1.1"\n'
      'creator="Runkeeper - http://www.runkeeper.com"\n'
      'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n'
      'xmlns="http://www.topografix.com/GPX/1/1"\n'
      'xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd"\n'
      'xmlns:gpxtpx="http://www.garmin.com/xmlschemas/TrackPointExtension/v1">\n'
      '<trk>\n'
      '<name><![CDATA[Running 8/7/17 8:11 pm]]></name>\n'
      '<time>2017-08-08T00:11:23Z</time>\n'
      '<trkseg>')

for i in d['activityDetailMetrics']:
    t = t+datetime.timedelta(0,i['metrics'][0])
    print('<trkpt lat="{lat}" lon="{lon}"><ele>{ele}</ele><time>{time}</time></trkpt>'.format(lat=i['metrics'][1], lon=i['metrics'][9], ele=i['metrics'][4], time=t.strftime("%Y-%m-%dT%H:%M:%SZ")))

print('</trkseg>\n'
      '</trk>\n'
      '</gpx>')
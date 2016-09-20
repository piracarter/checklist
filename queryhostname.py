#!/usr/bin/python
import urllib2, base64, json, sys
if len(sys.argv) < 4:
   print "Especificar hostname: queryhostname.py hostname timestamp-inicio timestamp-fin"
   sys.exit(2)
host = sys.argv[1]
inicio = sys.argv[2]
fin = sys.argv[3]
url = "http://150.100.38.232:8060/_search?size=10000&pretty=1&sort=@timestamp:asc&q=message:" + host + "%20AND%20@timestamp:%20[" + inicio + "%20TO%20" + fin +"]"
#print url
request = urllib2.Request(url)
base64string = base64.encodestring('%s:%s' % ("nagios2", "n4g10s16")).replace('\n', '')
request.add_header("Authorization", "Basic %s" % base64string)
result = urllib2.urlopen(request)
data = json.loads(result.read())
#print data
arr = []
i = 0
for item in data[u'hits'][u'hits']:
  arr.append([])
  arr[i].append(item[u'_source'][u'ram_o_average'])
  arr[i].append(item[u'_source'][u'ram_o_max'])
  arr[i].append(item[u'_source'][u'cpu_usage_1_average'])
  arr[i].append(item[u'_source'][u'cpu_usage_1_max'])
  arr[i].append(item[u'_source'][u'swap_usage_1_average'])
  arr[i].append(item[u'_source'][u'swap_usage_1_max'])
  arr[i].append(item[u'_source'][u'load_3_average'])
  arr[i].append(item[u'_source'][u'load_3_max'])
#  arr[i].append(item[u'_source'][u'ram_ptc_average'])
#  arr[i].append(item[u'_source'][u'ram_ptc_max'])
  message = item[u'_source'][u'message']
  bloque2 = "{" + message + "}"
  d = json.loads(bloque2)
  arr[i].append(d[u'timestamp'])
  i = i + 1

acum_cpu = 0
acum_load = 0
interval_max_swap = 0
picos = []
a = 0
for line in arr:
  acum_cpu = acum_cpu + line[2]
  acum_load = acum_load + line[6]
  if line[4] > interval_max_swap:
    interval_max_swap = line[4]
  if line[3] > 40:
    picos.append([])
    picos[a].append(line[8])
    picos[a].append(line[3])
    a = a + 1
if interval_max_swap > 0:
  print "Swap max: ", interval_max_swap
print host
print "Promedio CPU: ",acum_cpu / i
print "Promedio Load 15 min: ", acum_load /i
print "Intervalos: ", i
print "Picos: ", picos 

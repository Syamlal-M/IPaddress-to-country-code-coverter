import collections
import geoinfo

ipCounter = collections.Counter()

with open('access_log1','r') as fh:

  for logLine in fh:

    ip = logLine.split()[0]

    ipCounter.update([ip])

for ip,count in ipCounter.most_common(20):

    cName,cCode = geoinfo.country(ip=ip,key='8e9111c34830f5d4d5242e3dbba76a55')

    print('{:20} {:5} {}'.format(ip,count,cName))

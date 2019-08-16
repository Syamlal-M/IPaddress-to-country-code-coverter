# Fetch the country code of the IP address from the ipstack.com

 The python program is used to fetch the country name and code by sedning API KEY request to ipstack.com.Here I am using the collection module.
 I have created module a geoinfo to send API request and collect the information.
 
 ### Creating a module geoinfo
 
 ```python
 
 import requests

def country(*,ip=None,key=None):

  if ip != None and key != None:

    url = 'http://api.ipstack.com/{}?access_key={}'.format(ip,key)
    response = requests.get(url)
    geodata = response.json()

    country_name = geodata['country_name']
    country_code = geodata['country_code']

    return (country_name,country_code)

  else:

    return None
```

### Fetch the country code and name of the IP address

Here I am using log file access_log1 to take the IP address and collect the country code and name of the IP address from ipstack.com using API ACCESS KEY.

```python
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
    
   

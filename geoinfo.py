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

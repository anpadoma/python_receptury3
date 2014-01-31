# Proste żądania GET 

from urllib import request, parse

# Bazowy używany adres URL 
url = 'http://httpbin.org/get'

# Słownik z paramterami zapytania (jeśli są potrzebne)
parms = {
   'name1' : 'value1',
   'name2' : 'value2'
}

# Kodowanie łańcucha znaków z zapytaniem
querystring = parse.urlencode(parms)

# Zgłaszanie żądania GET i wczytywanie odpowiedzi
u = request.urlopen(url+'?' + querystring)
resp = u.read()

import json
from pprint import pprint

json_resp = json.loads(resp.decode('utf-8'))
pprint(json_resp)


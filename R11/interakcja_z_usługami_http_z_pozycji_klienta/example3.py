# Żądanie POST zgłaszane za pomocą biblioteki requests 
import requests

# Bazowy używany adres URL 
url = 'http://httpbin.org/post'

# Słownik z paramterami zapytania (jeśli są używane)
parms = {
   'name1' : 'value1',
   'name2' : 'value2'
}

# Dodatkowe nagłówki
headers = {
    'User-agent' : 'none/ofyourbusiness',
    'Spam' : 'Eggs'
}

resp = requests.post(url, data=parms, headers=headers)

# Odkodowany tekst zwracany przez żądanie
text = resp.text

from pprint import pprint
pprint(resp.json)

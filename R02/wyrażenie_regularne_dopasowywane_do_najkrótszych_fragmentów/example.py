# example.py
#
# Wyrażenie regularne wyszukujące najkrótsze pasujące fragmenty tekstu

import re

# Przykładowy tekst
text = 'Komputer mówi "nie." Telefon mówi "tak".'

# (a) Wyrażenie regularne znajdujące łańcuchy znaków w cudzysłowach (dopasowuje najdłuższy fragment)
str_pat = re.compile(r'\"(.*)\"')
print(str_pat.findall(text))

# (b) Wyrażenie regularne znajdujące łańcuchy znaków w cudzysłowach (dopasowuje najkrótszy fragment)
str_pat = re.compile(r'\"(.*?)\"')
print(str_pat.findall(text))




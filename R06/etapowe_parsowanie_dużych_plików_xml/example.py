# Stopniowe parsowanie danych w formacie XML
#
# Plik potholes.xml to znacznie zwięźlejsza wersja większego pliku,
# który można pobrać ze strony:
#
# https://data.cityofchicago.org/api/views/7as2-ds3y/rows.xml?accessType=DOWNLOAD

from xml.etree.ElementTree import iterparse

def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))
    # Pomijanie elementu nadrzędnego
    next(doc)

    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
                elem_stack[-2].remove(elem)
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass

# Ustalanie kodu pocztowego, dla którego zgłoszono najwięcej dziur

from collections import Counter
potholes_by_zip = Counter()

data = parse_and_remove('potholes.xml', 'row/row')
for pothole in data:
    potholes_by_zip[pothole.findtext('zip')] += 1

for zipcode, num in potholes_by_zip.most_common():
    print(zipcode, num)

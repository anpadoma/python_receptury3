# example.py
#
# Wczytywanie dokumentu XML, wprowadzanie w nim zmian i ponowne zapisywanie

from xml.etree.ElementTree import parse, Element
doc = parse('pred.xml')
root = doc.getroot()

# Usuwanie kilku elementów
root.remove(root.find('sri'))
root.remove(root.find('cr'))

# Wstawianie nowego elementu po <nm>...</nm>
nm_index = root.getchildren().index(root.find('nm'))

e = Element('spam')
e.text = 'To tylko test'
root.insert(nm_index + 1, e)

# Ponowne zapisywanie danych w pliku
doc.write('newpred.xml', xml_declaration=True)

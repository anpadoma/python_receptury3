from urllib.request import urlopen
from xml.etree.ElementTree import parse

# Pobieranie danych z kanału RSS i parsowanie ich
u = urlopen('http://planet.python.org/rss20.xml')
doc = parse(u)

# Pobieranie i wyświetlanie wybranych informacji
for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')

    print(title)
    print(date)
    print(link)
    print()

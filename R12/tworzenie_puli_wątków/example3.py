from concurrent.futures import ThreadPoolExecutor
import urllib.request

def fetch_url(url):
    u = urllib.request.urlopen(url)
    data = u.read()
    return data


pool = ThreadPoolExecutor(10)
# Przekazywanie zadania do puli
a = pool.submit(fetch_url, 'http://www.python.org')
b = pool.submit(fetch_url, 'http://www.pypy.org')

# Pobieranie wyników
x = a.result()
y = b.result()

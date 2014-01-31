# urlimport.py

import sys
import importlib.abc
import imp
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from html.parser import HTMLParser

# Debugowanie
import logging
log = logging.getLogger(__name__)

# Pobieranie odnośników z danego adresu URL
def _get_links(url):
    class LinkParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag == 'a':
                attrs = dict(attrs)
                links.add(attrs.get('href').rstrip('/'))

    links = set()
    try:
        log.debug('Pobieranie odnośników z %s' % url)
        u = urlopen(url)
        parser = LinkParser()
        parser.feed(u.read().decode('utf-8'))
    except Exception as e:
        log.debug('Nie można pobrać odnośników. %s', e)
    log.debug('Odnośniki: %r', links)
    return links

class UrlMetaFinder(importlib.abc.MetaPathFinder):
    def __init__(self, baseurl):
        self._baseurl = baseurl
        self._links   = { }
        self._loaders = { baseurl : UrlModuleLoader(baseurl) }

    def find_module(self, fullname, path=None):
        log.debug('find_module: fullname=%r, path=%r', fullname, path)
        if path is None:
            baseurl = self._baseurl
        else:
            if not path[0].startswith(self._baseurl):
                return None
            baseurl = path[0]

        parts = fullname.split('.')
        basename = parts[-1]
        log.debug('find_module: baseurl=%r, basename=%r', baseurl, basename)

        # Sprawdzanie pamięci podręcznej z odnośnikami
        if basename not in self._links:
            self._links[baseurl] = _get_links(baseurl)

        # Sprawdzanie, czy odnośnik prowadzi do pakietu
        if basename in self._links[baseurl]:
            log.debug('find_module: sprawdzanie pakietu %r', fullname)
            fullurl = self._baseurl + '/' + basename
            # Próba wczytania pakietu (powoduje dostęp do __init__.py)
            loader = UrlPackageLoader(fullurl)
            try:
                loader.load_module(fullname)
                self._links[fullurl] = _get_links(fullurl)
                self._loaders[fullurl] = UrlModuleLoader(fullurl)
                log.debug('find_module: wczytano pakiet %r', fullname)
            except ImportError as e:
                log.debug('find_module: nieudany import pakietu. %s', e)
                loader = None
            return loader

        # Zwykły moduł
        filename = basename + '.py'
        if filename in self._links[baseurl]:
            log.debug('find_module: znaleziono moduł %r', fullname)
            return self._loaders[baseurl]
        else:
            log.debug('find_module: nie znaleziono modułu %r', fullname)
            return None

    def invalidate_caches(self):
        log.debug('Unieważnianie pamięci podręcznej z odnośnikami')
        self._links.clear()

# Mechanizm wczytywania modułów na podstawie adresów URL
class UrlModuleLoader(importlib.abc.SourceLoader):
    def __init__(self, baseurl):
        self._baseurl = baseurl
        self._source_cache = {}

    def module_repr(self, module):
        return '<urlmodule %r from %r>' % (module.__name__, module.__file__)

    # Wymagana metoda
    def load_module(self, fullname):
        code = self.get_code(fullname)
        mod = sys.modules.setdefault(fullname, imp.new_module(fullname))
        mod.__file__ = self.get_filename(fullname)
        mod.__loader__ = self
        mod.__package__ = fullname.rpartition('.')[0]
        exec(code, mod.__dict__)
        return mod

    # Opcjonalne rozszerzenia
    def get_code(self, fullname):
        src = self.get_source(fullname)
        return compile(src, self.get_filename(fullname), 'exec')

    def get_data(self, path):
        pass

    def get_filename(self, fullname):
        return self._baseurl + '/' + fullname.split('.')[-1] + '.py'

    def get_source(self, fullname):
        filename = self.get_filename(fullname)
        log.debug('loader: odczyt %r', filename)
        if filename in self._source_cache:
            log.debug('loader: zapisano %r w pamięci podręcznej', filename)
            return self._source_cache[filename]
        try:
            u = urlopen(filename)
            source = u.read().decode('utf-8')
            log.debug('loader: wczytano %r', filename)
            self._source_cache[filename] = source
            return source
        except (HTTPError, URLError) as e:
            log.debug('loader: nieudane wczytywanie %r.  %s', filename, e)
            raise ImportError("Nie można wczytać %s" % filename)

    def is_package(self, fullname):
        return False

# Mechanizm wczytywania pakietów na podstawie adresów URL
class UrlPackageLoader(UrlModuleLoader):
    def load_module(self, fullname):
        mod = super().load_module(fullname)
        mod.__path__ = [ self._baseurl ]
        mod.__package__ = fullname

    def get_filename(self, fullname):
        return self._baseurl + '/' + '__init__.py'

    def is_package(self, fullname):
        return True

# Funkcje narzędziowe do instalowania i usuwania mechanizmu wczytywania
_installed_meta_cache = { }
def install_meta(address):
    if address not in _installed_meta_cache:
        finder = UrlMetaFinder(address)
        _installed_meta_cache[address] = finder
        sys.meta_path.append(finder)
        log.debug('%r zainstalowano w sys.meta_path', finder)
    
def remove_meta(address):
    if address in _installed_meta_cache:
        finder = _installed_meta_cache.pop(address)
        sys.meta_path.remove(finder)
        log.debug('%r usunięto z sys.meta_path', finder)

# Klasa do znajdowania ścieżek na podstawie adresu URL
class UrlPathFinder(importlib.abc.PathEntryFinder):
    def __init__(self, baseurl):
        self._links = None
        self._loader = UrlModuleLoader(baseurl)
        self._baseurl = baseurl

    def find_loader(self, fullname):
        log.debug('find_loader: %r', fullname)
        parts = fullname.split('.')
        basename = parts[-1]
        # Sprawdzanie pamięci podręcznej z odnośnikami
        if self._links is None:
            self._links = []     # Zobacz omówienie
            self._links = _get_links(self._baseurl)

        # Sprawdzanie, czy odnośnik prowadzi do pakietu
        if basename in self._links:
            log.debug('find_loader: sprawdzanie pakietu %r', fullname)
            fullurl = self._baseurl + '/' + basename
            # Próba wczytania pakietu (prowadzi do dostępu do __init__.py)
            loader = UrlPackageLoader(fullurl)
            try:
                loader.load_module(fullname)
                log.debug('find_loader: wczytano pakiet %r', fullname)
            except ImportError as e:
                log.debug('find_loader: %r to pakiet oparty na przestrzeni nazw', fullname)
                loader = None
            return (loader, [fullurl])

        # Zwykły moduł
        filename = basename + '.py'
        if filename in self._links:
            log.debug('find_loader: znaleziono moduł %r', fullname)
            return (self._loader, [])
        else:
            log.debug('find_loader: nie znaleziono modułu %r', fullname)
            return (None, [])

    def invalidate_caches(self):
        log.debug('Unieważnianie pamięci podręcznej z odnośnikami')
        self._links = None

# Sprawdzanie, czy ścieżka wygląda jak adres URL
_url_path_cache = {}
def handle_url(path):
    if path.startswith(('http://', 'https://')):
        log.debug('Obsługa ścieżki? %s. [Tak]', path)
        if path in _url_path_cache:
            finder = _url_path_cache[path]
        else:
            finder = UrlPathFinder(path)
            _url_path_cache[path] = finder
        return finder
    else:
        log.debug('Obsługa ścieżki? %s. [Nie]', path)

def install_path_hook():
    sys.path_hooks.append(handle_url)
    sys.path_importer_cache.clear()
    log.debug('Instalowanie handle_url')
    
def remove_path_hook():
    sys.path_hooks.remove(handle_url)
    sys.path_importer_cache.clear()
    log.debug('Usuwanie handle_url')

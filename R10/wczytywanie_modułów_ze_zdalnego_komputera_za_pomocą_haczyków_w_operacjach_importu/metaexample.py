# metaexample.py
#
# Przykład ilustrujący używanie importera ścieżek

# Rejestrowanie na poziomie DEBUG
if False:
    import logging
    logging.basicConfig(level=logging.DEBUG)

import urlimport
urlimport.install_meta('http://localhost:15000')

import fib
import spam
import grok.blah
print(grok.blah.__file__)

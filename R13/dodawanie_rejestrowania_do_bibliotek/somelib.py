# somelib.py

import logging
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

# Przykładowa funkcja (na potrzeby testów)
def func():
    log.critical("Błąd krytyczny!")
    log.debug("Komunikat diagnostyczny")

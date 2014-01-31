import logging
import logging.config

def main():
    # Konfigurowanie systemu rejestrowania operacji
    logging.config.fileConfig('logconfig.ini')

	# Zmienne (potrzebne w wywołaniach po wykonaniu zadania)
    hostname = 'www.python.org'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'

	# Przykładowe wywołania do rejestrowania operacji (należy je umieścić w programie)
    logging.critical('Nieznany host %s', hostname)
    logging.error("Nie można znaleźć %r", item)
    logging.warning('Funkcja jest przestarzała')
    logging.info('Otwieranie pliku %r w trybie %r', filename, mode)
    logging.debug('Kod dotarł do tego miejsca')

if __name__ == '__main__':
    main()

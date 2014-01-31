#!/usr/bin/env python3
# daemon.py

import os
import sys
import atexit
import signal

def daemonize(pidfile, *, stdin='/dev/null',
                          stdout='/dev/null',
                          stderr='/dev/null'):

    if os.path.exists(pidfile):
        raise RuntimeError('Już uruchomiono')

    # Pierwsze rozwidlenie (odłączenie od procesu nadrzędnego)
    try:
        if os.fork() > 0:
            raise SystemExit(0)   # Zakończenie pracy przez proces nadrzędny
    except OSError as e:
        raise RuntimeError('Rozwidlenie 1. nieudane.')
    
    os.chdir('/')
    os.umask(0)
    os.setsid()
	# Drugie rozwidlenie (rezygnacja z funkcji lidera sesji)
    try:
        if os.fork() > 0:
            raise SystemExit(0)
    except OSError as e:
        raise RuntimeError('Rozwidlenie 2. nieudane.')
    
	# Opróżnianie buforów wejścia-wyjścia
    sys.stdout.flush()
    sys.stderr.flush()

	# Zastępowanie deskryptorów plików dla strumieni stdin, stdout i stderr
    with open(stdin, 'rb', 0) as f:
        os.dup2(f.fileno(), sys.stdin.fileno())
    with open(stdout, 'ab', 0) as f:
        os.dup2(f.fileno(), sys.stdout.fileno())
    with open(stderr, 'ab', 0) as f:
        os.dup2(f.fileno(), sys.stderr.fileno())

	# Zapis pliku PID
    with open(pidfile,'w') as f:
        print(os.getpid(),file=f)

	# Przygotowanie do usuwania pliku PID w odpowiedzi na zakończenie pracy lub odpowiedni sygnał
    atexit.register(lambda: os.remove(pidfile))

	# Obsługa sygnału zakończenia pracy (wymagane)
    def sigterm_handler(signo, frame):
        raise SystemExit(1)

    signal.signal(signal.SIGTERM, sigterm_handler)

def main():
    import time
    sys.stdout.write('Demon rozpoczął pracę. Identyfiaktor pid: {}\n'.format(os.getpid()))
    while True:
        sys.stdout.write('Demon żyje! {}\n'.format(time.ctime()))
        time.sleep(10)

if __name__ == '__main__':
    PIDFILE = '/tmp/daemon.pid'

    if len(sys.argv) != 2:
        print('Stosowanie: {} [start|stop]'.format(sys.argv[0]), file=sys.stderr)
        raise SystemExit(1)

    if sys.argv[1] == 'start':
        try:
            daemonize(PIDFILE,
                      stdout='/tmp/daemon.log',
                      stderr='/tmp/dameon.log')
        except RuntimeError as e:
            print(e, file=sys.stderr)
            raise SystemExit(1)

        main()

    elif sys.argv[1] == 'stop':
        if os.path.exists(PIDFILE):
            with open(PIDFILE) as f:
                os.kill(int(f.read()), signal.SIGTERM)
        else:
            print('Nie działa', file=sys.stderr)
            raise SystemExit(1)

    else:
        print('Nieznane polecenie: {!r}'.format(sys.argv[1]), file=sys.stderr)
        raise SystemExit(1)


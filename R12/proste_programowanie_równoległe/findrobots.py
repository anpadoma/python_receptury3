# findrobots.py

import gzip
import io
import glob

def find_robots(filename):
    '''
	Wyszukiwanie w jednym pliku dziennika wszystkich hostów, które uzyskały dostęp do pliku robots.txt
    '''
    robots = set()
    with gzip.open(filename) as f:
        for line in io.TextIOWrapper(f,encoding='ascii'):
            fields = line.split()
            if fields[6] == '/robots.txt':
                robots.add(fields[0])
    return robots

def find_all_robots(logdir):
    '''
	Wyszukiwanie hostów we wszystkich plikach 
    '''
    files = glob.glob(logdir+"/*.log.gz")
    all_robots = set()
    for robots in map(find_robots, files):
        all_robots.update(robots)
    return all_robots

if __name__ == '__main__':
    import time
    start = time.time()
    robots = find_all_robots("logs")
    end = time.time()
    for ipaddr in robots:
        print(ipaddr)
    print('Czas wykonania: {:f} sekund'.format(end-start))


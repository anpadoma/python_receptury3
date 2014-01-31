import os
import fnmatch
import gzip
import bz2
import re

def gen_find(filepat, top):
    '''
    Wyszukuje w drzewie katalogów wszystkie nazwy plików pasujące do wzorca z symbolami
	wieloznacznymi powłoki
    '''
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path,name)

def gen_opener(filenames):
    '''
    Otwiera nazwy plików z sekwencji jedna po drugiej i tworzy obiekty plikowe.
    Plik jest zamykany natychmiast przy przechodzeniu do następnej iteracji. 
    '''
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        yield f
        f.close()

def gen_concatenate(iterators):
    '''
    Łączenie iteratorów w łańcuch.
    '''
    for it in iterators:
        yield from it

def gen_grep(pattern, lines):
    '''
    Wyszukiwanie w sekwencji wierszy tekstu pasującego do wyrażenia regularnego.
    '''
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line

if __name__ == '__main__':

    # Przykład 1.
    lognames = gen_find('access-log*', 'www')
    files = gen_opener(lognames)
    lines = gen_concatenate(files)
    pylines = gen_grep('(?i)python', lines)
    for line in pylines:
        print(line)

    # Przykład 2.
    lognames = gen_find('access-log*', 'www')
    files = gen_opener(lognames)
    lines = gen_concatenate(files)
    pylines = gen_grep('(?i)python', lines)
    bytecolumn = (line.rsplit(None,1)[1] for line in pylines)
    bytes = (int(x) for x in bytecolumn if x != '-')
    print('W sumie:', sum(bytes))

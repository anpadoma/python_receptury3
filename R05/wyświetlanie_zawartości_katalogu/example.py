# Wyświetlanie zawartości katalogu

import os
import os.path
import glob

pyfiles = glob.glob('*.py')

# Pobieranie wielkości plików i dat modyfikacji
name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name))
                for name in pyfiles]

for r in name_sz_date:
    print(r)

# Pobieranie metadanych
file_metadata = [(name, os.stat(name)) for name in pyfiles]
for name, meta in file_metadata:
    print(name, meta.st_size, meta.st_mtime)

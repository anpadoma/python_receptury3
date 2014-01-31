import subprocess

# Wysyłany tekst
text = b'''
Witaj, Polsko.
To tylko test.
Do zobaczenia.
'''

# Uruchamianie polecenia za pomocą potoków
p = subprocess.Popen(['wc'],
          stdout = subprocess.PIPE,
          stdin = subprocess.PIPE)

# Wysyłanie danych i pobieranie wyniku
stdout, stderr = p.communicate(text)

text = stdout.decode('utf-8')
print(text)


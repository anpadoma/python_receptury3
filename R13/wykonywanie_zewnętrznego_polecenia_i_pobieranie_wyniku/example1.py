import subprocess
try:
    out_bytes = subprocess.check_output(['netstat', '-a'])
    out_text = out_bytes.decode('utf-8')
    print(out_text)
except subprocess.CalledProcessError as e:
    print('Nie zadziałało. Powód:', e)
    print('Kod wyjścia:', e.returncode)


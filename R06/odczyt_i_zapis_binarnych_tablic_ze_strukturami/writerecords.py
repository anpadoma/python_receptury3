from struct import Struct

def write_records(records, format, f):
    '''
	Zapis sekwencji krotek do pliku binarnego ze strukturami
    '''
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))

# Przykład
if __name__ == '__main__':
    records = [ (1, 2.3, 4.5),
                (6, 7.8, 9.0),
                (12, 13.4, 56.7) ]

    with open('data.b', 'wb') as f:
         write_records(records, '<idd', f)

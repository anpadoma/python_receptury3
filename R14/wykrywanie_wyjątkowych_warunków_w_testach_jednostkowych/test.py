import unittest

# Prosta przykładowa funkcja
def parse_int(s):
    return int(s)

class TestConversion(unittest.TestCase):
	# Sprawdzanie, czy wyjątek jest zgłaszany
    def test_bad_int(self):
        self.assertRaises(ValueError, parse_int, "Brak")

	# Wykrywanie wyjątku z wykorzystaniem wyrażenia regularnego dla komunikatu o wyjątku
    def test_bad_int_msg(self):
        self.assertRaisesRegex(ValueError, 'invalid literal .*', parse_int, 'Brak') 

# Sprawdzanie wyjątku wraz z badaniem obiektu wyjątku
import errno

class TestIO(unittest.TestCase):
    def test_file_not_found(self):
        try:
            f = open('/file/not/found')
        except IOError as e:
            self.assertEqual(e.errno, errno.ENOENT)
        else:
            self.fail("Nie zgłoszono błędu IOError") 

if __name__ == '__main__':
    unittest.main()

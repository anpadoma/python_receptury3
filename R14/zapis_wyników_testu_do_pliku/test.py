import unittest

# Prosta przykładowa funkcja
def parse_int(s):
    return int(s)

class TestConversion(unittest.TestCase):
	# Sprawdzanie, czy wyjątek jest zgłaszany
    def test_bad_int(self):
        self.assertRaises(ValueError, parse_int, "Brak")

	# Testowanie wyjątku z wykorzystaniem wyrażenia regularnego dla komunikatu o wyjątku
    def test_bad_int_msg(self):
        self.assertRaisesRegex(ValueError, 'invalid literal .*', parse_int, 'Brak') 

# Testowanie wyjątku wraz z badaniem obiektu wyjątku
import errno

class TestIO(unittest.TestCase):
    def test_file_not_found(self):
        try:
            f = open('/file/not/found')
        except IOError as e:
            self.assertEqual(e.errno, errno.ENOENT)
        else:
            self.fail("Nie zgłoszono wyjątku IOError") 

import sys
def main(out=sys.stderr, verbosity=2):
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out, verbosity=verbosity).run(suite)

if __name__ == '__main__':
    with open('testing.out', 'w') as f:
        main(f)

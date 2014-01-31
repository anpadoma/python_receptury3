import unittest
import os
import platform

class Tests(unittest.TestCase):
    def test_0(self):
        self.assertTrue(True)

    @unittest.skip('Pominięty test')
    def test_1(self):
        self.fail("Powinien zakończyć się niepowodzeniem!")

    @unittest.skipIf(os.name=='posix', 'Nieobsługiwane w systemach uniksowych')
    def test_2(self):
        import winreg

    @unittest.skipUnless(platform.system() == 'Darwin', 'Test dla systemu Mac OS X')
    def test_3(self):
        self.assertTrue(True)

    @unittest.expectedFailure
    def test_4(self):
        self.assertEqual(2+2, 5)

if __name__ == '__main__':
    unittest.main(verbosity=2)

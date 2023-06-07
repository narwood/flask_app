from translator import frenchToEnglish, englishToFrench
import unittest

class Test_F2E(unittest.TestCase):
    def test_b2h(self):
        self.assertEqual('hello', frenchToEnglish('bonjour'))

    def test_a2g(self):
        self.assertEqual('goodbye', frenchToEnglish('au revoir'))



class Test_E2F(unittest.TestCase):
    def test_h2b(self):
        self.assertEqual('bonjour', englishToFrench('hello'))

    def test_g2a(self):
        self.assertEqual('au revoir', englishToFrench('goodbye'))


if __name__ == '__main__':
    unittest.main()
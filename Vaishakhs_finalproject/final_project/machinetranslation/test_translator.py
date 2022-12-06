import unittest
from translator import french_to_english
from translator import english_to_french
 
class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("cette fleur est très belle"), "this flower is very beautiful")
        self.assertNotEqual(french_to_english("cette fleur est très belle"), "this flower is very beautiful")
class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("this flower is very beautiful"), "cette fleur est très belle")
        self.assertNotEqual(french_to_english("this flower is very beautiful"), "cette fleur est très belle")
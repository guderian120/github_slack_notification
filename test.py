import unittest
from cool_function import CoolClass

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Runs before each test method"""
        self.cool_instance = CoolClass()
       

    def test_statement_returned(self):
        self.assertEqual(self.cool_instance.cool_attribute(), "This is a cool attribute!")
     

if __name__ == '__main__':
    unittest.main()
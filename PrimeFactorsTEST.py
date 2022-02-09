import unittest
from PrimeFactors import *

class PrimeFactorsTEST(unittest.TestCase):
    def test_negative(self):
        value = -43
        with self.assertRaises(Exception):
            PrimeFactors(value)
    
    def test_zero(self):
        value = 0
        with self.assertRaises(Exception):
            PrimeFactors(value)
            
    def test_one_float(self):
        value = 1.0
        self.assertEqual([], PrimeFactors(value))
    
    def test_two(self):
        value = 2
        self.assertEqual([2], PrimeFactors(value))
        
    def test_four(self):
        value = 4
        self.assertEqual([2,2],PrimeFactors(value))
        
    def test_eight(self):
        value = 8
        self.assertEqual([2,2,2],PrimeFactors(value))
        
    if __name__ == '__main__':
        unittest.main()
        
            
    
        
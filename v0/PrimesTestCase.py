import unittest 
from prime import is_prime 

class PrimesTestCase(unittest.TestCase):
	def test_is_five_prime(self):
		self.assertTrue(is_prime(5)) 
	   
   #<Include your test here>
	def test_is_twentyseven_prime(self):
		self.assertTrue(is_prime(27))

	def test_is_one_prime(self):
		self.assertTrue(is_prime(1))

	def test_is_negative_prime(self):
		self.assertTrue(is_prime(-1))

	def test_is_zero_prime(self):
		self.assertTrue(is_prime(0))


   

   

if __name__ == '__main__':
	unittest.main()

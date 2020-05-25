import unittest
import BernieGray_Python1 as BG

class TestFunc(unittest.TestCase):

	def test_func(self):
		self.assertEqual(BG.func({1:2, 3:4}, [1,3]), True)
		self.assertEqual(BG.func({1:2, 3:4}, [1,2]), False)
		self.assertEqual(BG.func({-1:2, 3:4}, [-1,3]), True)
		self.assertEqual(BG.func({0:2, 3:4}, [1,3]), False)
		self.assertEqual(BG.func({0:2}, [0]), True)






if __name__ == '__main__':
	unittest.main()

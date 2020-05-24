import unittest
import JackHarris_Python1 as JH

class TestCalc(unittest.TestCase):

	def test_string_num(self):
		self.assertEqual(JH.string_num(['5','1','9','10']), ['1','5','9','10'])
		self.assertEqual(JH.string_num(['100','1000','200','8000']), ['100','200','1000','8000'])
		self.assertEqual(JH.string_num(['1','-1','0']), ['-1','0','1'])





if __name__ == '__main__':
	unittest.main()

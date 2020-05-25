import unittest
import NinaXu_Python1 as NX

class TestWordList(unittest.TestCase):

	def test_word_list(self):
		self.assertEqual(NX.word_list('Hello. How are you.','you'), ['How are you'])






if __name__ == '__main__':
	unittest.main()

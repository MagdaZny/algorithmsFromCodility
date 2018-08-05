import unittest
from src.TapeEquilibrium import solution

class TestTapeEquilibrium(unittest.TestCase):

    def test_two_elements_array(self):
        self.assertEqual(1, solution([1,2]))

    def test_three_elements_array(self):
        self.assertEqual(2, solution([1,2,5]))

    def test_five_elements_array(self):
        self.assertEqual(1, solution([3,1,2,4,3]))
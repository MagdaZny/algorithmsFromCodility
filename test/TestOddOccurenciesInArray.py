import unittest
from src.OddOccurenriesInArray import solution


class TestOddOccurenciesArray(unittest.TestCase):

    def test_return_itself_wnen_one_element_in_array(self):
        self.assertEqual(1, solution([1]))

    def test_return_one_wnen_three_elements_in_array(self):
        self.assertEqual(1, solution([3,3,1]))

    def test_return_one_wnen_three_elements_in_array2(self):
        self.assertEqual(1, solution([9,3,9,3,1]))


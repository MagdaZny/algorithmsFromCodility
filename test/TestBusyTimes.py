import unittest
from src.BusyTimes import solve


class TestTask1(unittest.TestCase):

    def test_no_ids(self):
        self.assertEqual("2018-01-01", solve(["2018-01-01 2018-01-03"]))


    def test_no_ids(self):
        self.assertEqual("2018-01-02", solve(["2018-01-01 2018-01-03", "2018-01-02 2018-01-03"]))


    def test_no_ids(self):
        self.assertEqual("2018-01-03", solve(["2018-01-03 2018-01-05", "2018-01-02 2018-01-08", "2018-01-03 2018-01-03"]))



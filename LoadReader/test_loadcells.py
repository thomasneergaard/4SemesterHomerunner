import unittest
from app import loadcells

class TestLoadcell(unittest.TestCase):

    def setUp(self):
        self.loadcell = Loadcells()

    def test_zero_weight(self):
        self.assertEqual(self.loadcell.get_weight_in_kg(0), 0)

    def test_negative_weight(self):
        self.assertEqual(self.loadcell.get_weight_in_kg(-50), 0)

    def test_positive_weight(self):
        self.assertAlmostEqual(self.loadcell.get_weight_in_kg(1000), 1.0)

    def test_float_weight(self):
        self.assertAlmostEqual(self.loadcell.get_weight_in_kg(1234.5), 1.2345)

if __name__ == "__main__":
    unittest.main()
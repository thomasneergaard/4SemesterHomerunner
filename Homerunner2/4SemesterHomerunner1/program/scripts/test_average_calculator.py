import sys
import unittest
from unittest.mock import MagicMock, patch


mock_loadcells = MagicMock()
sys.modules['loadcells'] = mock_loadcells


import average_calculator as ac
import custom_exceptions


class TestAverageCalculator(unittest.TestCase):
    def setUp(self):
        ac.queue_capacity = 10
        ac.queue = ac.Queue(ac.queue_capacity)
        ac.full_sum = 0
        mock_loadcells.get_weight_in_kg.return_value = 10  # <- ensure return value

    def fill_queue(self, values):
        for v in values:
            ac.queue.put(v)
            ac.full_sum += v

    def test_add_normal_number(self):
        self.fill_queue([10, 10, 10, 10, 10])
        ac.add_number(11)
        self.assertEqual(ac.queue.qsize(), 6)
        self.assertIn(11, list(ac.queue.queue))

    def test_high_deviation_raises(self):
        self.fill_queue([10] * 10)  # Fill to capacity
        with self.assertRaises(custom_exceptions.number_deviation_high):
            ac.number_deviation_high(10.7)

    def test_low_deviation_raises(self):
        self.fill_queue([10] * 10)  # Fill to capacity
        with self.assertRaises(custom_exceptions.number_deviation_low):
            ac.number_deviation_low(9.2)

    def test_queue_rollover(self):
        self.fill_queue([10] * 10)
        ac.add_number(10)  # Should remove one and add new one
        self.assertEqual(ac.queue.qsize(), 10)
        self.assertEqual(ac.full_sum, 100)

    def test_get_queue_average_empty(self):
        self.assertEqual(ac.get_queue_average(), 0)

    def test_get_queue_average_non_empty(self):
        self.fill_queue([10, 20, 30])
        self.assertEqual(ac.get_queue_average(), 20)

    def test_get_weight_number(self):
        result = ac.get_weight_number()
        self.assertEqual(result, 10)
        self.assertEqual(ac.queue.qsize(), 1)
        self.assertIn(10, list(ac.queue.queue))
        mock_loadcells.get_weight_in_kg.assert_called_once()


if __name__ == '__main__':
    unittest.main()

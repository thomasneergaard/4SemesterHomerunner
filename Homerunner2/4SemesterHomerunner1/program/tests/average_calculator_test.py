import unittest
import scripts
import custom_exceptions
import sys
sys.path.insert(0, 'denne pc/3rd semester projekt/4SemesterHomerunner/4SemesterHomerunner1/program/scripts')

class TestAverageCalculator(unittest.TestCase):
    def setUp(self):
        ac.queue = ac.Queue(ac.queue_capacity)
        ac.full_sum = 0

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
        self.fill_queue([10] * 9)
        with self.assertRaises(custom_exceptions.number_deviation_high):
            ac.number_deviation_high(15)

    def test_low_deviation_raises(self):
        self.fill_queue([10] * 9)
        with self.assertRaises(custom_exceptions.number_deviation_low):
            ac.number_deviation_low(7)

    def test_queue_rollover(self):
        self.fill_queue([10] * 10)
        ac.add_number(10)
        self.assertEqual(ac.queue.qsize(), 10)
        self.assertEqual(ac.full_sum, 100)

    def test_get_queue_average_empty(self):
        self.assertEqual(ac.get_queue_average(), 0)

    def test_get_queue_average_non_empty(self):
        self.fill_queue([10, 20, 30])
        self.assertEqual(ac.get_queue_average(), 20)

    def test_max_weight_not_triggered(self):
        self.fill_queue([40] * 5)
        try:
            ac.max_weight_reached()
        except Exception:
            self.fail("max_weight_reached() should not raise with avg < max_weight")

    def test_max_weight_triggered(self):
        self.fill_queue([1500] * 10)
        with self.assertRaises(custom_exceptions.weight_too_heavy):
            ac.max_weight_reached()

if __name__ == '__main__':
    unittest.main()
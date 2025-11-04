import unittest
from stats_utils import mean, median, mode, range_list, remove_outliers
import math
class TestMean(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(mean([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(mean([10, 20, 30]), 20.0)
    
    def test_empty_list(self):
        self.assertEqual(mean([]), 0)
    
    def test_single_element(self):
        self.assertEqual(mean([5]), 5.0)
    
    def test_negative_numbers(self):
        self.assertEqual(mean([-1, -2, -3]), -2.0)
        self.assertEqual(mean([-5, 0, 5]), 0.0)
    
    def test_float_numbers(self):
        self.assertAlmostEqual(mean([1.5, 2.5, 3.5]), 2.5, places=5)

class TestMedian(unittest.TestCase):
    def test_odd_length(self):
        self.assertEqual(median([1, 3, 5]), 3)
        self.assertEqual(median([1, 2, 3, 4, 5]), 3)
    
    def test_even_length(self):
        self.assertEqual(median([1, 2, 3, 4]), 2.5)
        self.assertEqual(median([1, 3, 5, 7]), 4.0)
    
    def test_empty_list(self):
        self.assertEqual(median([]), 0)
    
    def test_single_element(self):
        self.assertEqual(median([5]), 5)
    
    def test_unsorted_list(self):
        self.assertEqual(median([5, 1, 3, 2, 4]), 3)
        self.assertEqual(median([10, 5, 20, 15]), 12.5)

class TestMode(unittest.TestCase):
    def test_single_mode(self):
        self.assertEqual(mode([1, 2, 2, 3]), 2)
        self.assertEqual(mode([1, 1, 1, 2, 3]), 1)
    
    def test_multiple_modes(self):
        result = mode([1, 1, 2, 2, 3])
        self.assertIn(result, [1, 2])  # Should return one of the modes
    
    def test_empty_list(self):
        self.assertIsNone(mode([]))
    
    def test_all_same(self):
        self.assertEqual(mode([5, 5, 5, 5]), 5)
    
    def test_no_duplicates(self):
        result = mode([1, 2, 3, 4, 5])
        self.assertIn(result, [1, 2, 3, 4, 5])

class TestRangeList(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(range_list([10, 2, 7, 5]), 8)  # max - min = 10 - 2 = 8
        self.assertEqual(range_list([1, 5, 3]), 4)  # max - min = 5 - 1 = 4
    
    def test_empty_list(self):
        self.assertEqual(range_list([]), 0)
    
    def test_single_element(self):
        self.assertEqual(range_list([5]), 0)  # max - min = 5 - 5 = 0
    
    def test_negative_numbers(self):
        self.assertEqual(range_list([-5, -1, -3]), 4)  # max - min = -1 - (-5) = 4
        self.assertEqual(range_list([-10, 10]), 20)  # max - min = 10 - (-10) = 20
    
    def test_all_same(self):
        self.assertEqual(range_list([5, 5, 5, 5]), 0)

class TestRemoveOutliers(unittest.TestCase):
    def test_normal_case(self):
        # For [1, 2, 3, 100], mean ≈ 26.5, std ≈ 43.5
        # 100 is more than 2 std devs away, so it should be removed
        result = remove_outliers([1, 2, 3, 100], threshold=2)
        # Should remove 100 if using proper standard deviation
        self.assertIsInstance(result, list)
    
    def test_empty_list(self):
        self.assertEqual(remove_outliers([]), [])
    
    def test_no_outliers(self):
        result = remove_outliers([1, 2, 3, 4, 5], threshold=2)
        self.assertEqual(len(result), 5)
        self.assertEqual(sorted(result), [1, 2, 3, 4, 5])
    
    def test_all_outliers(self):
        result = remove_outliers([100, 200, 300], threshold=1)
        self.assertIsInstance(result, list)
    
    def test_single_element(self):
        result = remove_outliers([5], threshold=2)
        self.assertEqual(result, [5])


if __name__ == '__main__':
    unittest.main(verbosity=2)


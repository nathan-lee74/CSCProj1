import unittest
import data
import main


expense_sum = {'Bills': 0.0,
               'Donation': 10.9,
               'Entertainment': 211.84,
               'Food': 473.15,
               'Grocery': 41.13,
               'Supplies': 43.9,
               'Shopping': 0.0,
               'Sports': 50.0,
               'Travel': 226.21,
               'Misc': 9.99,
               'Not Listed': 13.78}

total_counts = {'Bills': 0.0,
                'Donation': 1.0,
                'Entertainment': 9.0,
                'Food': 23.0,
                'Grocery': 3.0,
                'Supplies': 4.0,
                'Shopping': 0.0,
                'Sports': 2.0,
                'Travel': 2.0,
                'Misc': 1.0,
                'Not Listed': 1.0}


class TestCases(unittest.TestCase):

    # Summation tests
    def test_sum_1(self):
        result = main.sums(data.main_data, data.totals)
        self.assertEqual(expense_sum, result)

    def test_sum_2(self):
        result = main.sums(data.main_data, data.totals)
        self.assertNotEqual({}, result)

    # Count tests
    def test_count_1(self):
        result = main.counts(data.main_data, data.counts)
        self.assertEqual(total_counts, result)

    def test_count_2(self):
        result = main.counts(data.main_data, data.counts)
        self.assertNotEqual(total_counts, result)

if __name__ == '__main__':
        unittest.main()

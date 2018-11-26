import unittest

def my_sum(x, y):
    return x + y

class TestMySum(unittest.TestCase):
    def test_two_plus_two(self):
        result = my_sum(2, 2)
        self.assertEqual(result, 4)

unittest.main()

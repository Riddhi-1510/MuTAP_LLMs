import unittest

def function_put(a, b, c):
    if a >= b and a >= c:
        return "a is the greatest"
    elif b >= a and b >= c:
        return "b is the greatest"
    else:
        return "c is the greatest"

class TestFunctionPut(unittest.TestCase):
    def test_all_cases(self):
        self.assertEqual(function_put(10, 5, 3), "a is the greatest")
        self.assertEqual(function_put(1, 5, 3), "b is the greatest")
        self.assertEqual(function_put(1, 2, 5), "c is the greatest")
        self.assertEqual(function_put(5,5,5), "a is the greatest")
        self.assertEqual(function_put(2, 10, 1), "b is the greatest")
        self.assertEqual(function_put(-5, -10, -2), "a is the greatest")
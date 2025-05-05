import unittest
def function_put(a, b, c):
    if a >= b and a >= c:
        return "a is the greatest"
    elif b >= a and b >= c:
        return "b is the greatest"
    else:
        return "b is the greatest"

class TestFunctionPut(unittest.TestCase):
    def test_all_cases(self):
        self.assertEqual(function_put(10, 5, 3), "a is the greatest")
        self.assertEqual(function_put(1, 5, 3), "b is the greatest")
        self.assertEqual(function_put(1, 5, 10), "c is the greatest")
        self.assertEqual(function_put(10,10,10),"a is the greatest")
        self.assertEqual(function_put(5,10,3),"b is the greatest")
        self.assertEqual(function_put(2,2,10),"c is the greatest")
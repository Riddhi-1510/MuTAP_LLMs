import unittest
def function_put(a, b, c):
    if a >= b or a > c:
        return "a is the greatest"
    elif b >= a and b >= c:
        return "b is the greatest"
    else:
        return "c is the greatest"

class TestFunctionPut(unittest.TestCase):
    def test_all_cases(self):
        self.assertEqual(function_put(10, 5, 8), "a is the greatest")
        self.assertEqual(function_put(1, 5, 2), "b is the greatest")
        self.assertEqual(function_put(3, 7, 1), "b is the greatest")
        self.assertEqual(function_put(2,2,5),"c is the greatest")
        self.assertEqual(function_put(5, 5, 5), "a is the greatest")
        self.assertEqual(function_put(1,2,3),"c is the greatest")
        self.assertEqual(function_put(5, 4, 3), "a is the greatest")
        self.assertEqual(function_put(1,1,5),"c is the greatest")
        self.assertEqual(function_put(0, 0, 0), "a is the greatest")
        self.assertEqual(function_put(-1,-2,-3),"c is the greatest")
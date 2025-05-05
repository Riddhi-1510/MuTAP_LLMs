import unittest
def function_put(a, b, c) -> str:
    if not all(isinstance(x, int) and not isinstance(x, bool) for x in [a,b,c]):
        raise TypeError("All inputs must be integers (bool is not allowed).")
    elif not all(x > 0 for x in [a, b, c]):
        raise ValueError("All sides must be greater than zero.")
    elif a + b <= c or a + c <= b or b + c <= a:
        return "Not a valid triangle"
    elif a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    return "Scalene"

class TestFunctionPut(unittest.TestCase):
    def test_all_cases(self):
        self.assertEqual(function_put(2, 2, 2), "Equilateral")
        self.assertEqual(function_put(3, 4, 5), "Scalene")
        self.assertEqual(function_put(2, 3, 2), "Isosceles")
        self.assertRaises(ValueError, function_put, 1, 2, -1)
        self.assertRaises(TypeError, function_put, 1, 2, True)
        self.assertEqual(function_put(1,1,2),"Isosceles")
        self.assertEqual(function_put(1, 5, 2), "Not a valid triangle")
        self.assertRaises(ValueError, function_put, 0,1,1)
        self.assertRaises(TypeError, function_put, 1, 'a', 1)
        self.assertEqual(function_put(5,5,8),"Isosceles")
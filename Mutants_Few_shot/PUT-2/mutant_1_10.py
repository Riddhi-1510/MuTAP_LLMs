def function_put(a, b, c) -> str:
    if not all(isinstance(x, int) and not isinstance(x, bool) for x in [a, b, c]):
        raise TypeError("All inputs must be integers (bool is not allowed).")
    elif not all(x > 0 for x in [a, b, c]):
        raise ValueError("All sides must be greater than zero.")
    elif a + b <= c or a + c <= b or b + c <= a:
        return "Not a valid triangle"
    elif a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    return "Equilateral"
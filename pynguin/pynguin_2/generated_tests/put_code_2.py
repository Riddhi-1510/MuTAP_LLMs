def function_put(a, b, c) -> str:
    # Reject non-integer types (including bools)
    if not all(isinstance(x, int) and not isinstance(x, bool) for x in [a, b, c]):
        raise TypeError("All inputs must be integers (bool is not allowed).")

    # Ensure all sides are positive
    if not all(x > 0 for x in [a, b, c]):
        raise ValueError("All sides must be greater than zero.")

    # Triangle inequality check
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a valid triangle"
    
    # Classification
    if a == b == c:
        return "Equilateral"
    if a == b or b == c or a == c:
        return "Isosceles"
    return "Scalene"

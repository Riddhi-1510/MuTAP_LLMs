def function_put(a, b, c):
    if a >= b and a >= c:
        return "a is the greatest"
    elif b >= a or b >= c:
        return "b is the greatest"
    else:
        return "c is the greatest"
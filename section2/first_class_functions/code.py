"""
    First class functions means that these functions can be passed around
    as variables to other functions just like other variables.
"""

def divide(dividend, divisor):
    if divisor < 1:
        raise ZeroDivisionError ("Divisor cannot be zero.")

    return dividend / divisor

def calculate(*values, operator):
    return operator(*values)

result = calculate(20, 4, operator=divide)
print(f"Result = {result:.3f}")

__author__ = 'LENOVO'

(lambda x, y: x + y)(45, 67)

"""
    Lambda functions can also be assigned to variables.
"""

add = lambda a, b: a + b

print("Addition of 3 and 4: ", add(3, 4))

def double_num(a):
    return a * 2

sequence = list(range(10))
print(f"Base sequence: {sequence}\n\n")
# Using List comprehension.
print("Doubled numbers using list comprehension:", [double_num(x) for x in sequence],"\n")

# Using "map" function
print("Doubled numbers using map function:", list(map(double_num, sequence)), "\n")

# Using lambda function
print("Doubled numbers using lambda function in list comprehension:", [(lambda x: x * 2)(x) for x in sequence], "\n")

# Using a lambda function inside the map function
print("Doubled numbers using lambda function inside the map function:", list(map(lambda x: x * 2, sequence)))

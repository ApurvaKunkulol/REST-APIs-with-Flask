__author__ = 'LENOVO'

def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total *= arg
    return total


print(multiply(3))

# Using an Asterik to pass unpacked variables to the function.
def add(a, b):
    return a + b

print(add(*[5, 4])) # When the Asteriksign is used before the list while calling the function
                    # and passing the argument list to it, it will unfold the list and assign each element to
                    # the parameter.

# In case of a dictionary, two asterik marks have to be used to unfold it while passing it to a function call.
params = {"a": 6, "b":7}
print(add(**params))


def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(*args)
    else:
        print("No valid operator provided to apply.")


print(apply(1, 2, 3, 4, 5, 6, operator="*"))

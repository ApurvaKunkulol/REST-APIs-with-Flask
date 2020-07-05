__author__ = 'LENOVO'

def named(**kwargs):
    print(kwargs)


named(name="Bob", age=25)


def named2(name, age):
    print(name, age)

details = {"name": "Bob", "age": 25}
named2(details, 25)    # <- This kind of passing will result in unexpected behaviour.

named2(**details)
def print_nicely(**kwargs):
    named(**kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_nicely(name="Bob", age=45)

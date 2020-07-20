__author__ = 'Apurva A Kunkulol.'

#  Using f-strings in Python.


name = "Bob"

greeting = "Hello Bob"

print("Name: {}\n".format(name))
print("Greeting: {}\n".format(greeting))


greeting = f"Hello {name}\n"

print("Greeting: ", greeting)

name = "Rolf"
greeting = f"Hello {name}\n"
print("Updated greeting: ", greeting)


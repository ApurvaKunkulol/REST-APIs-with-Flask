__author__ = 'LENOVO'

friend_ages = {"Rolf": 24, "Adam": 40, "Anne": 27}
print("Adam's age: ", friend_ages["Adam"])

# List of dictionaries.
friends = [
    {"name": "Adam", "age": 28},
    {"name": "Ajit", "age": 34},
    {"name": "Saurabh", "age": 27},
    {"name": "Anne", "age": 26}
]

attendance = {"Bob": 96, "Rolf": 80, "Anne": 100}
for student in attendance:
    print(f"{student}: {attendance[student]}")

# Proper way

print()
for student, age in attendance.items():
    print(f"{student}: {age}")


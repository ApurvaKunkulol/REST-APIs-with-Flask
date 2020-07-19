def divide(dividend, divisor):
    if divisor < 1:
        raise ZeroDivisionError("Divisor cannot be less than 1.")
        return
    return dividend / divisor

students = [
    {"name":"Bob", "grades": [75, 90]},
    {"name": "Rolf", "grades": []},
    {"name": "Jen", "grades": [100, 90]}
]

try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide(sum(grades), len(grades))
        print(f"{name}'s average score is {average}.")
except ZeroDivisionError as zerr:
    print(f"ERROR: {name} has no grades yet!")
else:
    print("-- All student averages calculated --")
finally:
    print("-- End of student average calculation. --")

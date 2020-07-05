__author__ = 'LENOVO'


grades = [35, 67, 98, 100, 100]

total = 0
amount = len(grades)
for grade in grades:
    total += grade

print("The average grade is: ", total / amount)
total = sum(grades)
print("The average grade is: ", total / amount)



class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)



apurva = Student("Apurva", (90, 90, 93, 78, 90))
bobby = Student("Bobby", (87, 76, 77, 45, 32, 44))

for stud in [apurva, bobby]:
    print(f"Details of {stud.name}")
    print(f"\tGrades: {stud.grades}")
    print(f"\tAverage of grades: {stud.average():.3f}\n\n")

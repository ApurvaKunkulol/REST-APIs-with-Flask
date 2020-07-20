from typing import List


class Student:
    def __init__(self, name: str, grades: List[int] = []):
        self.name = name
        self.grades = grades

    def take_exam(self, result: int):
        self.grades.append(result)

bob = Student("Bob")
bob.take_exam(45)
print(f"Bob's grades: {bob.grades}")
ralph = Student("Ralph")
print(f"Ralph's grades: {ralph.grades}")
anshu = Student("Anshu")
anshu.take_exam(85)
print(f"Anshu's grades: {anshu.grades}\n\nRalph's grades: {ralph.grades}" +
f"\n\nBob's grades: {bob.grades}")

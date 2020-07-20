from typing import List, Optional


class Student:
    def __init__(self, name: str, grades: Optional[List[int]] = None):
        self.name = name
        self.grades = grades or []

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

from typing import List

class Student:
    def __init__(self, name: str, grades: List[int] = None):
        self.name = name
        self.grades = grades or []

    def take_exam(self,result):
        self.grades.append(result)

bob = Student("Bob")
bob.take_exam(90)
print (bob.grades)
print (id(bob.grades))

charlie = Student("Charlie")
print (charlie.grades)
print (id(charlie.grades))
class Student:
    def __init__(self, studentname, grades): # init can have also parameters
        self.name = studentname
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

student = Student("Bob",(90,90,93,78,90,85))
print(student.name) # Rolf comes out
print(student.grades) # (90, 90, 93, 78, 90)
print(student.average_grade()) # Calling method inside class

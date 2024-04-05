class Student:
    roll = ""
    age = ""
    gpa = ""


rahim = Student()
print(isinstance(rahim, Student))
rahim.age = 25
rahim.gpa = 3.95
rahim.roll = 1003
print(f"Roll : {rahim.roll}, Age : {rahim.age}, GPA : {rahim.gpa} ")

karim = Student()
# print(isinstance(karim, Student))
karim.age = 27
karim.gpa = 3.85
karim.roll = 1005
print(f"Roll : {karim.roll}, Age : {karim.age}, GPA : {karim.gpa} ")
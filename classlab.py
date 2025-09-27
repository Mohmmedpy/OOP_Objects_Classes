class Student:
    school = "AI University"
    student_count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.student_count += 1


s1 = Student("Ali", 21)
s2 = Student("Sara", 22)

print("Student 1:", s1.name, s1.age, s1.school)
print("Student 2:", s2.name, s2.age, s2.school)

s1.age = 23
print("\nAfter changing s1's age:")
print("s1.age =", s1.age)
print("s2.age =", s2.age)

Student.school = "Tuwaiq Academy"
print("\nAfter changing class variable 'school':")
print("s1.school =", s1.school)
print("s2.school =", s2.school)

print("\nTotal number of students:", Student.student_count)

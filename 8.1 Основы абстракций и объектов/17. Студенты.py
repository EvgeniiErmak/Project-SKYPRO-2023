class Student:

    def __init__(self, name, course):
        self.name = name
        self.course = course

student_1 = Student("Алиса", 3)
student_2 = Student("Маргарита", 2)


# Не удаляйте этот код, он нужен для проверки

print(student_1.name, student_1.course)
print(student_2.name, student_2.course)
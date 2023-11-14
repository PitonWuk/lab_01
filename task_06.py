"""
Завдання 6
Створіть клас Student, який має атрибути name, age,
grade та courses. Реалізуйте метод класу add_course, який
додає новий предмет до списку курсів студента
"""
class Student:
    def __init__(self, name, age, grade, courses):
        self.name = name
        self.age = age
        self.grade = grade
        self.courses = []

    @classmethod
    def add_course(cls, student, course):
        student.courses.append(course)
        print(f"Student {student.name} got one more course: {course}")

student1 = Student("Mark", 19, 80, "Math")

Student.add_course(student1, "Litr")

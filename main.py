import uuid
"""ITF 08 Final Project Attendance System
# TODO 1 Enter your name and submission date
Name : Amna ELNaami
Delivery Date : 8 31 23
"""

# TODO 2 Define Course Class and define constructor with
class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = uuid.uuid4()
        self.course_name = course_name
        self.course_mark = course_mark

course_name = input("Enter the course name: ")
course_mark = input("Enter the course mark: ")

course = Course(course_name, course_mark)
print("Course ID:", course.course_id)
print("Course Name:", course.course_name)
print("Course Mark:", course.course_mark)

class Student:
    # TODO 3 define static variable indicates total student count
    total_students = 0
    # TODO 4 define a constructor which includes
    # student_id (unique using uuid module)
    # student_name (user input)
    # student_age (user input)
    # student_number (user_input)
    # courses_list (List of Course Objects)
    def __init__(self, student_name, student_age, student_number, courses_list):
        self.student_id = uuid.uuid4()
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = courses_list
        Student.total_students += 1

student_name = input("Enter student name: ")
student_age = int(input("Enter student age: "))
student_number = input("Enter student number: ")
courses_list = []
student = Student(student_name, student_age, student_number, courses_list)
print("Student name "+student_name)
print("Student age "+str(student_age))
print("Student number "+student_number)
print("Total students:", Student.total_students)


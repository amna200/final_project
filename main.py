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
    def __init__(self, student_name, student_age, student_number, courses_list=None):
        self.student_id = uuid.uuid4()
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = courses_list
        self.courses_list = courses_list if courses_list is not None else []
        Student.total_students += 1

    def enroll_course(self, course):
        self.courses_list.append(course)

    def get_student_details(self):
        return self.__dict__

    def get_student_courses(self):
        return self.courses_list

    def print_student_courses(self):
        print("Student Courses:")
        for course in self.courses_list:
            print(f"Course: {course.course_name}, Mark: {course.course_mark}")

    def get_student_average(self):
        total_marks = sum(int(course.course_mark) for course in self.courses_list)
        if self.courses_list:
            return total_marks / len(self.courses_list)
        else:
            return 0

student_name = input("Enter student name: ")
student_age = int(input("Enter student age: "))
student_number = input("Enter student number: ")
courses_list = []
student = Student(student_name, student_age, student_number, courses_list)
print("Student name "+student_name)
print("Student age "+str(student_age))
print("Student number "+student_number)
print("Total students:", Student.total_students)
student.enroll_course(course)
print("Student Details:", student.get_student_details())
print("Student Courses:", student.get_student_courses())
course1_name = input("Enter course 1 name: ")
course1_mark = input("Enter course 1 mark: ")
course1 = Course(course1_name, course1_mark)
student.enroll_course(course1)
course2_name = input("Enter course 2 name: ")
course2_mark = input("Enter course 2 mark: ")
course2 = Course(course2_name, course2_mark)
student.enroll_course(course2)

student.print_student_courses()
average = student.get_student_average()
print("Student Average Mark:", average)

# TODO 8 declare empty students list
students = []

while True:


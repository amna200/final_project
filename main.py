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


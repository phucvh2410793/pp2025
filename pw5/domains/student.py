import math

class Student:
    def __init__(self, sid, name, dob):
        self.id = sid
        self.name = name
        self.dob = dob
        self.marks = {}
        self.gpa = 0

    def set_mark(self, course_id, mark):
        mark = math.floor(mark * 10) / 10   
        self.marks[course_id] = mark

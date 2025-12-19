class Student:
    def __init__(self, sid, name, dob):
        self.id = sid
        self.name = name
        self.dob = dob

    def input(self):
        self.id = input("ID: ")
        self.name = input("Name: ")
        self.dob = input("Date of birth: ")

    def list(self):
        print(self.id, self.name, self.dob)
class Course:
    def __init__(self, cid, name):
        self.id = cid
        self.name = name
        self.marks = {}

    def input(self):
        self.id = input("ID: ")
        self.name = input("Name: ")

    def list(self):
        print(self.id, self.name)
class StudentMarkManager:
    def __init__(self):
        self.students = []
        self.courses = []
    def input_students(self):
        n = int(input("Number of students: "))
        for _ in range(n):
            s = Student("", "", "")
            s.input()
            self.students.append(s)
    def input_courses(self):
        m = int(input("Number of courses: "))
        for _ in range(m):
            c = Course("", "")
            c.input()
            self.courses.append(c)
    def input_marks(self):
        cid = input("Course ID: ")
        course = next((c for c in self.courses if c.id == cid), None)

        if not course:
            print("Course not found")
            return

        for s in self.students:
            score = float(input(f"Mark for {s.name}: "))
            course.marks[s.id] = score
    def list_students(self):
        for s in self.students:
            s.list()

    def list_courses(self):
        for c in self.courses:
            c.list()
    def show_marks(self):
        cid = input("Course ID: ")
        course = next((c for c in self.courses if c.id == cid), None)

        if not course:
            print("Course not found")
            return

        for s in self.students:
            print(s.name, ":", course.marks.get(s.id, "N/A"))
manager = StudentMarkManager()


while True:
    print("\n1. Input students")
    print("2. Input courses")
    print("3. Input marks")
    print("4. List students")
    print("5. List courses")
    print("6. Show marks")
    print("0. Exit")

    choice = input("Choose: ")

    if choice == "1":
        manager.input_students()
    elif choice == "2":
        manager.input_courses()
    elif choice == "3":
        manager.input_marks()
    elif choice == "4":
        manager.list_students()
    elif choice == "5":
        manager.list_courses()
    elif choice == "6":
        manager.show_marks()
    elif choice == "0":
        break

import math
def input_marks(self):
    cid = input("Course ID: ")
    course = next((c for c in self.courses if c.id == cid), None)

    if not course:
        print("Course not found")
        return

    for s in self.students:
        raw = float(input(f"Mark for {s.name}: "))
        rounded = math.floor(raw * 10) / 10
        course.marks[s.id] = rounded
import numpy as np
class Course:
    def __init__(self, cid, name, credit):
        self.id = cid
        self.name = name
        self.credit = credit
        self.marks = {}

    def input(self):
        self.id = input("ID: ")
        self.name = input("Name: ")
        self.credit = int(input("Credits: "))
def calculate_gpa(self, student_id):
    scores = []
    credits = []

    for c in self.courses:
        if student_id in c.marks:
            scores.append(c.marks[student_id])
            credits.append(c.credit)

    if not scores:
        return 0

    scores = np.array(scores)
    credits = np.array(credits)

    return np.sum(scores * credits) / np.sum(credits)
def sort_students_by_gpa(self):
    self.students.sort(
        key=lambda s: self.calculate_gpa(s.id),
        reverse=True
    )
def list_students_with_gpa(self):
    for s in self.students:
        gpa = self.calculate_gpa(s.id)
        print(s.name, "- GPA:", round(gpa, 2))
import curses

def curses_menu(stdscr):
    stdscr.clear()
    stdscr.addstr(1, 5, "STUDENT MARK MANAGEMENT", curses.A_BOLD)
    stdscr.addstr(3, 5, "1. Input students")
    stdscr.addstr(4, 5, "2. Input courses")
    stdscr.addstr(5, 5, "3. Input marks")
    stdscr.addstr(6, 5, "4. List students by GPA")
    stdscr.addstr(7, 5, "0. Exit")
    stdscr.refresh()
    stdscr.getch()
curses.wrapper(curses_menu)

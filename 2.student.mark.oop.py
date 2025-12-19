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
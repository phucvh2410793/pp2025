def input_students():
    from domains.student import Student
    n = int(input("Enter number of students: "))
    students = []

    for _ in range(n):
        sid = input("Student ID: ")
        name = input("Name: ")
        dob = input("DOB: ")
        students.append(Student(sid, name, dob))

    return students


def input_courses():
    from domains.course import Course
    m = int(input("Enter number of courses: "))
    courses = []

    for _ in range(m):
        cid = input("Course ID: ")
        name = input("Course name: ")
        credit = int(input("Credit: "))
        courses.append(Course(cid, name, credit))

    return courses


def input_marks(students, courses):
    for c in courses:
        print(f"\n--- Course {c.name} ---")
        for s in students:
            score = float(input(f"Mark for {s.name}: "))
            s.set_mark(c.id, score)

def input_students():
    from domains.student import Student
    students = []
    n = int(input("Enter number of students: "))

    for _ in range(n):
        sid = input("Student ID: ")
        name = input("Name: ")
        dob = input("DOB: ")
        students.append(Student(sid, name, dob))

    # write students.txt
    with open("students.txt", "w") as f:
        for s in students:
            f.write(f"{s.id},{s.name},{s.dob}\n")

    return students


def input_courses():
    from domains.course import Course
    courses = []
    m = int(input("Enter number of courses: "))

    for _ in range(m):
        cid = input("Course ID: ")
        name = input("Course name: ")
        credit = int(input("Credit: "))
        courses.append(Course(cid, name, credit))

    # write courses.txt
    with open("courses.txt", "w") as f:
        for c in courses:
            f.write(f"{c.id},{c.name},{c.credit}\n")

    return courses


def input_marks(students, courses):
    with open("marks.txt", "w") as f:
        for c in courses:
            for s in students:
                score = float(input(f"Mark for {s.name} in {c.name}: "))
                s.set_mark(c.id, score)
                f.write(f"{s.id},{c.id},{score}\n")
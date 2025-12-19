def input_students():
    from domains.student import Student
    n = int(input("Enter number of students: "))
    students = []

    for _ in range(n):
        sid = input("Student ID: ")
        name = input("Student Name: ")
        dob = input("Date of Birth: ")
        students.append(Student(sid, name, dob))

    return students


def input_courses():
    from domains.course import Course
    m = int(input("Enter number of courses: "))
    courses = []

    for _ in range(m):
        cid = input("Course ID: ")
        name = input("Course Name: ")
        credit = int(input("Credit: "))
        courses.append(Course(cid, name, credit))

    return courses


def input_marks(students, courses):
    print("\n--- ENTER MARKS ---")
    for course in courses:
        print(f"\nCourse: {course.name} ({course.id})")
        for stu in students:
            score = float(input(f"Enter mark for {stu.name}: "))
            stu.set_mark(course.id, score)
from input import input_students, input_courses, input_marks
from output import show_students
from domains.mark import calculate_gpa


def main():
    print("=== STUDENT MANAGEMENT SYSTEM ===")

    students = input_students()
    courses = input_courses()

    input_marks(students, courses)

    for stu in students:
        calculate_gpa(stu, courses)

    students.sort(key=lambda s: s.gpa, reverse=True)

    show_students(students)


if __name__ == "__main__":
    main()
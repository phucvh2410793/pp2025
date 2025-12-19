import os

from input import input_students, input_courses, input_marks
from domains.mark import calculate_gpa
from persistence import AsyncPersistence

DATA_FILE = "students.dat"


def main():
    store = AsyncPersistence(DATA_FILE)

    try:
        if os.path.exists(DATA_FILE):
            print("Found students.dat -> loading (pickle + compression in background system)...")
            data = store.load(default={"students": [], "courses": []})
            students = data.get("students", [])
            courses = data.get("courses", [])

            print(f"Loaded {len(students)} students and {len(courses)} courses.")
            for s in students:
                print(f"{s.id} - {s.name} | GPA: {s.gpa}")
            return

        print("No students.dat -> input new data...")
        students = input_students()
        courses = input_courses()
        marks = input_marks(students, courses)

        calculate_gpa(students, courses, marks)

        store.request_save({
            "students": students,
            "courses": courses
        })

        print("Saved (async) to students.dat")

    finally:
        store.close()


if __name__ == "__main__":
    main()

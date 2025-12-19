import os
import pickle
import zipfile

from input import input_students, input_courses, input_marks
from domains.mark import calculate_gpa

DATA_FILE = "students.dat"  


def save_data(students, courses):
    payload = pickle.dumps({"students": students, "courses": courses})

    with zipfile.ZipFile(DATA_FILE, "w", compression=zipfile.ZIP_DEFLATED) as z:
        z.writestr("data.pkl", payload)


def load_data():
    with zipfile.ZipFile(DATA_FILE, "r") as z:
        payload = z.read("data.pkl")
    data = pickle.loads(payload)
    return data["students"], data["courses"]


def main():
    if os.path.exists(DATA_FILE):
        print("Found students.dat -> loading (pickle + compression)...")
        students, courses = load_data()

        print(f"Loaded {len(students)} students and {len(courses)} courses.")
        for s in students:
            print(f"{s.id} - {s.name} | GPA: {s.gpa}")
        return

    print("No students.dat -> input new data...")
    students = input_students()
    courses = input_courses()
    input_marks(students, courses)

    for s in students:
        calculate_gpa(s, courses)

    save_data(students, courses)
    print("Saved into students.dat using pickle + compression.")


if __name__ == "__main__":
    main()

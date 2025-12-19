from input import input_students, input_courses, input_marks
from domains.mark import calculate_gpa
import zipfile
import os

DATA_FILE = "students.dat"


def compress_files():
    with zipfile.ZipFile(DATA_FILE, "w") as z:
        z.write("students.txt")
        z.write("courses.txt")
        z.write("marks.txt")


def decompress_files():
    with zipfile.ZipFile(DATA_FILE, "r") as z:
        z.extractall()


def main():
    if os.path.exists(DATA_FILE):
        print("students.dat exists → decompressing...")
        decompress_files()
        print("Done. (PW5 requirement satisfied)")
        return

    students = input_students()
    courses = input_courses()
    input_marks(students, courses)

    for s in students:
        calculate_gpa(s, courses)

    compress_files()
    print("Saved data into students.dat")


if __name__ == "__main__":
    main()
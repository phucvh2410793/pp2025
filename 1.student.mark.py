students = []
courses = []
marks = []    

def input_number_of_students():
    n = int(input("Enter number of students: "))
    return n


def input_student_info():
    sid = input("Student ID: ")
    name = input("Student name: ")
    dob = input("Student DoB: ")
    student = {"id": sid, "name": name, "dob": dob}
    students.append(student)


def input_number_of_courses():
    n = int(input("Enter number of courses: "))
    return n


def input_course_info():
    cid = input("Course ID: ")
    name = input("Course name: ")
    course = {"id": cid, "name": name}
    courses.append(course)


def input_marks_for_course():
    course_id = input("Enter course ID to input marks: ")

    course_ids = [c["id"] for c in courses]
    if course_id not in course_ids:
        print("Course not found!")
        return

    print(f"Entering marks for course: {course_id}")

    for s in students:
        mark = float(input(f"Mark for student {s['id']} - {s['name']}: "))
        marks.append({
            "course_id": course_id,
            "student_id": s["id"],
            "mark": mark
        })



def list_courses():
    print("\n--- List of Courses ---")
    for c in courses:
        print(f"- {c['id']} | {c['name']}")
    print("-----------------------")


def list_students():
    print("\n--- List of Students ---")
    for s in students:
        print(f"- {s['id']} | {s['name']} | DoB: {s['dob']}")
    print("------------------------")


def show_marks_for_course():
    course_id = input("Enter course ID to show marks: ")

    print(f"\n--- Marks for Course {course_id} ---")
    for m in marks:
        if m["course_id"] == course_id:
            stu = next(s for s in students if s["id"] == m["student_id"])
            print(f"{stu['id']} - {stu['name']}: {m['mark']}")
    print("------------------------------------")



def main():
    n_students = input_number_of_students()
    for _ in range(n_students):
        input_student_info()
      
    n_courses = input_number_of_courses()
    for _ in range(n_courses):
        input_course_info()

    while True:
        print("\nSelect option:")
        print("1. Input marks for a course")
        print("2. List students")
        print("3. List courses")
        print("4. Show marks for a given course")
        print("0. Exit")

        choice = input("Your choice: ")
        if choice == "1":
            input_marks_for_course()
        elif choice == "2":
            list_students()
        elif choice == "3":
            list_courses()
        elif choice == "4":
            show_marks_for_course()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

 
if __name__ == "__main__":
    main()

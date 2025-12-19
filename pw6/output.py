def show_students(students):
    print("\n--- STUDENT LIST SORTED BY GPA ---")
    for stu in students:
        print(f"{stu.id} - {stu.name} | GPA: {stu.gpa}")

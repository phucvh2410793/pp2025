import tkinter as tk
from tkinter import messagebox

from input import input_students, input_courses, input_marks
from domains.mark import calculate_gpa
from persistence import AsyncPersistence

DATA_FILE = "students.dat"


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")

        self.store = AsyncPersistence(DATA_FILE)
        data = self.store.load(default={"students": [], "courses": []})
        self.students = data["students"]
        self.courses = data["courses"]

        tk.Button(root, text="Input students", command=self.add_students).pack(fill="x")
        tk.Button(root, text="Input courses", command=self.add_courses).pack(fill="x")
        tk.Button(root, text="Input marks + GPA", command=self.add_marks).pack(fill="x")
        tk.Button(root, text="Show students", command=self.show_students).pack(fill="x")
        tk.Button(root, text="Exit", command=self.exit_app).pack(fill="x")

    def add_students(self):
        self.students = input_students()
        self.save()

    def add_courses(self):
        self.courses = input_courses()
        self.save()

    def add_marks(self):
        marks = input_marks(self.students, self.courses)
        calculate_gpa(self.students, self.courses, marks)
        self.save()

    def show_students(self):
        if not self.students:
            messagebox.showinfo("Info", "No students")
            return
        text = "\n".join(
            f"{s.id} - {s.name} | GPA: {s.gpa}" for s in self.students
        )
        messagebox.showinfo("Students", text)

    def save(self):
        self.store.request_save({
            "students": self.students,
            "courses": self.courses
        })

    def exit_app(self):
        self.store.close()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

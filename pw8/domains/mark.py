import numpy as np
import math


def calculate_gpa(student, courses):
    credit_dict = {c.id: c.credit for c in courses}

    marks = np.array([student.marks[c] for c in student.marks])
    credits = np.array([credit_dict[c] for c in student.marks])

    weighted = marks * credits
    gpa = weighted.sum() / credits.sum()

    student.gpa = math.floor(gpa * 10) / 10
